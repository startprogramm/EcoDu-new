from django.contrib import admin
from .models import Quiz, Question, Answer, QuizAttempt, UserAnswer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4
    fields = ['text', 'is_correct']


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    fields = ['text', 'order']
    show_change_link = True


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'video', 'passing_score', 'get_total_questions', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'video__title']
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['quiz', 'text_preview', 'order']
    list_filter = ['quiz']
    search_fields = ['text', 'quiz__title']
    inlines = [AnswerInline]
    
    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Question'


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'text', 'is_correct']
    list_filter = ['is_correct']
    search_fields = ['text', 'question__text']


class UserAnswerInline(admin.TabularInline):
    model = UserAnswer
    extra = 0
    fields = ['question', 'selected_answer', 'is_correct']
    readonly_fields = ['is_correct']


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ['user', 'quiz', 'score', 'passed', 'correct_answers', 'total_questions', 'completed_at']
    list_filter = ['passed', 'completed_at']
    search_fields = ['user__username', 'quiz__title']
    readonly_fields = ['score', 'passed', 'completed_at']
    inlines = [UserAnswerInline]


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ['attempt', 'question', 'selected_answer', 'is_correct']
    list_filter = ['is_correct']
    search_fields = ['attempt__user__username', 'question__text']
