from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Category(models.Model):
    """Video categories for organizing content"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon class")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']


class Video(models.Model):
    """Main video model"""
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, db_index=True)
    description = models.TextField()
    youtube_url = models.URLField(help_text="YouTube embed URL (e.g., https://www.youtube.com/embed/VIDEO_ID)")
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='videos', db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='authored_videos')
    author_name = models.CharField(max_length=100, blank=True)
    author_role = models.CharField(max_length=100, blank=True, default="Video developer")
    author_image = models.ImageField(upload_to='authors/', blank=True)
    views = models.IntegerField(default=0, db_index=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    def get_like_percentage(self):
        total = self.likes + self.dislikes
        if total == 0:
            return 0
        return int((self.likes / total) * 100)
    
    class Meta:
        ordering = ['-created_at']


class VideoProgress(models.Model):
    """Track user progress on videos"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='video_progress')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='user_progress')
    completed = models.BooleanField(default=False)
    watched_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.video.title}"
    
    class Meta:
        unique_together = ['user', 'video']
        verbose_name_plural = 'Video Progress'


class VideoRating(models.Model):
    """Track user likes/dislikes on videos"""
    RATING_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='video_ratings')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='ratings')
    rating = models.CharField(max_length=10, choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.video.title} ({self.rating})"
    
    class Meta:
        unique_together = ['user', 'video']


class Comment(models.Model):
    """Video comments with reply support"""
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} on {self.video.title}"
    
    class Meta:
        ordering = ['-created_at']
