from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import models
from .models import Quiz, Question, QuizAttempt, UserAnswer
from videos.models import Video


@login_required
def take_quiz(request, video_slug):
    """Take a quiz for a video"""
    video = get_object_or_404(Video, slug=video_slug)
    quiz = get_object_or_404(Quiz, video=video)
    questions = quiz.questions.all().prefetch_related('answers')
    
    context = {
        'video': video,
        'quiz': quiz,
        'questions': questions,
    }
    return render(request, 'quizzes/take_quiz.html', context)


@login_required
def submit_quiz(request, quiz_id):
    """Submit quiz answers and calculate score (AJAX)"""
    if request.method == 'POST':
        quiz = get_object_or_404(Quiz, id=quiz_id)
        questions = quiz.questions.all()
        
        correct_count = 0
        total_questions = questions.count()
        
        # Create quiz attempt
        attempt = QuizAttempt.objects.create(
            user=request.user,
            quiz=quiz,
            score=0,  # Will be updated
            passed=False,  # Will be updated
            total_questions=total_questions
        )
        
        # Process each answer
        for question in questions:
            answer_id = request.POST.get(f'question_{question.id}')
            if answer_id:
                try:
                    from .models import Answer
                    selected_answer = Answer.objects.get(id=answer_id, question=question)
                    
                    # Create user answer record
                    UserAnswer.objects.create(
                        attempt=attempt,
                        question=question,
                        selected_answer=selected_answer,
                        is_correct=selected_answer.is_correct
                    )
                    
                    if selected_answer.is_correct:
                        correct_count += 1
                except Answer.DoesNotExist:
                    pass
        
        # Calculate score
        score = int((correct_count / total_questions) * 100) if total_questions > 0 else 0
        attempt.score = score
        attempt.correct_answers = correct_count
        attempt.passed = score >= quiz.passing_score
        attempt.save()
        
        # Update user stats
        if attempt.passed:
            request.user.quizzes_passed = QuizAttempt.objects.filter(
                user=request.user, passed=True
            ).count()
            request.user.total_points += 10  # Award points for passing
            request.user.save()
        
        return JsonResponse({
            'success': True,
            'score': score,
            'correct': correct_count,
            'total': total_questions,
            'passed': attempt.passed,
            'passing_score': quiz.passing_score,
        })
    
    return JsonResponse({'success': False}, status=400)


@login_required
def quiz_results(request, attempt_id):
    """View quiz results"""
    attempt = get_object_or_404(QuizAttempt, id=attempt_id, user=request.user)
    user_answers = attempt.user_answers.all().select_related('question', 'selected_answer')
    
    context = {
        'attempt': attempt,
        'user_answers': user_answers,
    }
    return render(request, 'quizzes/quiz_results.html', context)


@login_required
def leaderboard(request):
    """Quiz leaderboard showing top scorers"""
    from django.db.models import Count, Avg
    from users.models import CustomUser
    
    # Get users with most quizzes passed
    top_users = CustomUser.objects.annotate(
        passed_count=Count('quiz_attempts', filter=models.Q(quiz_attempts__passed=True)),
        avg_score=Avg('quiz_attempts__score')
    ).filter(passed_count__gt=0).order_by('-passed_count', '-avg_score')[:10]
    
    context = {
        'top_users': top_users,
    }
    return render(request, 'quizzes/leaderboard.html', context)
