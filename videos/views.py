from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q, Prefetch
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator
from .models import Video, Category, VideoProgress, VideoRating, Comment
from quizzes.models import Quiz


@cache_page(60 * 5)  # Cache for 5 minutes
def home(request):
    """Homepage with video categories and featured videos"""
    # Optimize queries: prefetch related data to avoid N+1
    categories = Category.objects.prefetch_related('videos').all()
    featured_videos = Video.objects.select_related('category', 'author').order_by('-created_at')[:8]
    
    context = {
        'categories': categories,
        'featured_videos': featured_videos,
    }
    return render(request, 'videos/home.html', context)


def video_detail(request, slug):
    """Video detail page with player, description, and related videos"""
    # Optimize: select_related for ForeignKey fields
    video = get_object_or_404(
        Video.objects.select_related('category', 'author').prefetch_related('comments'),
        slug=slug
    )
    
    # Increment view count (don't load other fields)
    video.views = video.views + 1
    video.save(update_fields=['views'])
    
    # Get related videos with optimization
    related_videos = Video.objects.select_related('category', 'author').exclude(id=video.id).order_by('-created_at')[:4]
    
    # Get only parent comments with optimization
    comments = video.comments.select_related('user').filter(parent=None).order_by('-created_at')[:50]
    
    # Check if user has completed this video (optimize with get instead of filter.first())
    completed = False
    user_rating = None
    if request.user.is_authenticated:
        try:
            progress = VideoProgress.objects.get(user=request.user, video=video)
            completed = progress.completed
        except VideoProgress.DoesNotExist:
            pass
        
        try:
            rating = VideoRating.objects.get(user=request.user, video=video)
            user_rating = rating.rating
        except VideoRating.DoesNotExist:
            pass
    
    # Check if video has a quiz - use try/except to handle RelatedObjectDoesNotExist
    has_quiz = False
    try:
        has_quiz = video.quiz is not None
    except:
        has_quiz = False
    
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
    """List all videos in a category with pagination"""
    category = get_object_or_404(Category, slug=slug)
    
    # Optimize: select_related and add pagination
    videos_query = Video.objects.select_related('category', 'author').filter(category=category).order_by('-created_at')
    
    # Pagination: 12 videos per page
    paginator = Paginator(videos_query, 12)
    page_number = request.GET.get('page', 1)
    videos = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'videos': videos,
    }
    return render(request, 'videos/category_videos.html', context)


def search_videos(request):
    """Search videos by title or description with pagination"""
    query = request.GET.get('q', '')
    
    if query:
        # Optimize search with select_related
        videos_query = Video.objects.select_related('category', 'author').filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        ).order_by('-created_at')
    else:
        videos_query = Video.objects.none()
    
    # Pagination: 12 videos per page
    paginator = Paginator(videos_query, 12)
    page_number = request.GET.get('page', 1)
    videos = paginator.get_page(page_number)
    
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
        
        if not progress.completed:  # Only save if state changed
            progress.completed = True
            progress.save(update_fields=['completed'])
            
            # Update user stats efficiently using database aggregation
            from django.db.models import Count
            completed_count = VideoProgress.objects.filter(
                user=request.user, completed=True
            ).count()
            request.user.videos_watched = completed_count
            request.user.save(update_fields=['videos_watched'])
        
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
