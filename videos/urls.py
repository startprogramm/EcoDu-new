from django.urls import path
from . import views

app_name = 'videos'

urlpatterns = [
    path('', views.home, name='home'),
    path('video/<slug:slug>/', views.video_detail, name='video_detail'),
    path('category/<slug:slug>/', views.category_videos, name='category_videos'),
    path('search/', views.search_videos, name='search'),
    
    # AJAX endpoints
    path('api/like/<int:video_id>/', views.toggle_like, name='toggle_like'),
    path('api/complete/<int:video_id>/', views.mark_complete, name='mark_complete'),
    path('api/comment/<int:video_id>/', views.add_comment, name='add_comment'),
]
