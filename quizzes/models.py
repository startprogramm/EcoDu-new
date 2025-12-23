from django.db import models
from django.conf import settings
from videos.models import Video


class Quiz(models.Model):
    """Quiz associated with a video"""
    video = models.OneToOneField(Video, on_delete=models.CASCADE, related_name='quiz')
    title = models.CharField(max_length=200)
    passing_score = models.IntegerField(default=70, help_text="Percentage required to pass")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Quiz: {self.title}"
    
    def get_total_questions(self):
        return self.questions.count()
    
    class Meta:
        verbose_name_plural = 'Quizzes'


class Question(models.Model):
    """Quiz question"""
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    order = models.IntegerField(default=0, help_text="Display order of question")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Q{self.order}: {self.text[:50]}"
    
    def get_correct_answer(self):
        return self.answers.filter(is_correct=True).first()
    
    class Meta:
        ordering = ['order']


class Answer(models.Model):
    """Answer option for a question"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.text} ({'Correct' if self.is_correct else 'Wrong'})"


class QuizAttempt(models.Model):
    """Track user quiz attempts and scores"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='quiz_attempts')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='attempts')
    score = models.IntegerField(help_text="Score as percentage")
    passed = models.BooleanField()
    correct_answers = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    completed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} ({self.score}%)"
    
    def save(self, *args, **kwargs):
        # Calculate if passed based on score
        self.passed = self.score >= self.quiz.passing_score
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-completed_at']


class UserAnswer(models.Model):
    """Track individual answers in a quiz attempt"""
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name='user_answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_correct = models.BooleanField()
    
    def __str__(self):
        return f"{self.attempt.user.username} - Q{self.question.order}"
    
    def save(self, *args, **kwargs):
        # Auto-determine if answer is correct
        self.is_correct = self.selected_answer.is_correct
        super().save(*args, **kwargs)
