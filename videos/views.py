from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from .models import Video, Category, VideoProgress, VideoRating, Comment
from quizzes.models import Quiz


def home(request):
    """Homepage with video categories and featured videos"""
    categories = Category.objects.all()
    featured_videos = Video.objects.all()[:8]
    
    context = {
        'categories': categories,
        'featured_videos': featured_videos,
    }
    return render(request, 'videos/home.html', context)


def video_detail(request, slug):
    """Video detail page with player, description, and related videos"""
    video = get_object_or_404(Video, slug=slug)
    
    # Increment view count
    video.views += 1
    video.save(update_fields=['views'])
    
    # Get related videos from same category
    related_videos = Video.objects.filter(category=video.category).exclude(id=video.id)[:4]
    
    # Get comments
    comments = video.comments.filter(parent=None).order_by('-created_at')
    
    # Check if user has completed this video
    completed = False
    user_rating = None
    if request.user.is_authenticated:
        progress = VideoProgress.objects.filter(user=request.user, video=video).first()
        completed = progress.completed if progress else False
        
        rating = VideoRating.objects.filter(user=request.user, video=video).first()
        user_rating = rating.rating if rating else None
    
    # Check if video has a quiz
    has_quiz = hasattr(video, 'quiz')
    
    context = {
        'video': video,
        'related_videos': related_videos,
        'comments': comments,
        'completed': completed,
        'user_rating': user_rating,
        'has_quiz': has_quiz,
    }
    return render(request, 'videos/video_detail.html', context)


def category_videos(request, slug):
    """List all videos in a category"""
    category = get_object_or_404(Category, slug=slug)
    videos = Video.objects.filter(category=category)
    
    context = {
        'category': category,
        'videos': videos,
    }
    return render(request, 'videos/category_videos.html', context)


def search_videos(request):
    """Search videos by title or description"""
    query = request.GET.get('q', '')
    videos = Video.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    ) if query else Video.objects.none()
    
    context = {
        'query': query,
        'videos': videos,
    }
    return render(request, 'videos/search_results.html', context)


@login_required
def toggle_like(request, video_id):
    """Toggle like/dislike on a video (AJAX)"""
    if request.method == 'POST':
        video = get_object_or_404(Video, id=video_id)
        rating_type = request.POST.get('rating')  # 'like' or 'dislike'
        
        # Get or create rating
        rating, created = VideoRating.objects.get_or_create(
            user=request.user,
            video=video,
            defaults={'rating': rating_type}
        )
        
        if not created:
            # If rating exists and is the same, remove it
            if rating.rating == rating_type:
                rating.delete()
                # Update video counts
                if rating_type == 'like':
                    video.likes -= 1
                else:
                    video.dislikes -= 1
            else:
                # Change rating
                old_rating = rating.rating
                rating.rating = rating_type
                rating.save()
                
                # Update video counts
                if old_rating == 'like':
                    video.likes -= 1
                    video.dislikes += 1
                else:
                    video.likes += 1
                    video.dislikes -= 1
        else:
            # New rating
            if rating_type == 'like':
                video.likes += 1
            else:
                video.dislikes += 1
        
        video.save()
        
        return JsonResponse({
            'success': True,
            'likes': video.likes,
            'dislikes': video.dislikes,
        })
    
    return JsonResponse({'success': False}, status=400)


@login_required
def mark_complete(request, video_id):
    """Mark a video as completed (AJAX)"""
    if request.method == 'POST':
        video = get_object_or_404(Video, id=video_id)
        
        progress, created = VideoProgress.objects.get_or_create(
            user=request.user,
            video=video
        )
        
        progress.completed = True
        progress.save()
        
        # Update user stats
        request.user.videos_watched = VideoProgress.objects.filter(
            user=request.user, completed=True
        ).count()
        request.user.save()
        
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False}, status=400)


@login_required
def add_comment(request, video_id):
    """Add a comment to a video (AJAX)"""
    if request.method == 'POST':
        video = get_object_or_404(Video, id=video_id)
        text = request.POST.get('text', '').strip()
        parent_id = request.POST.get('parent_id')
        
        if text:
            comment = Comment.objects.create(
                video=video,
                user=request.user,
                text=text,
                parent_id=parent_id if parent_id else None
            )
            
            return JsonResponse({
                'success': True,
                'comment': {
                    'id': comment.id,
                    'user': comment.user.username,
                    'text': comment.text,
                    'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M'),
                }
            })
    
    return JsonResponse({'success': False}, status=400)
