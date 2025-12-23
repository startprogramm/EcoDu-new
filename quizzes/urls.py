from django.urls import path
from . import views

app_name = 'quizzes'

urlpatterns = [
    path('take/<slug:video_slug>/', views.take_quiz, name='take_quiz'),
    path('submit/<int:quiz_id>/', views.submit_quiz, name='submit_quiz'),
    path('results/<int:attempt_id>/', views.quiz_results, name='quiz_results'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
