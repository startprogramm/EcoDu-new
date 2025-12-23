from django.contrib import admin
from .models import Category, Video, VideoProgress, VideoRating, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ['user', 'text', 'created_at']
    readonly_fields = ['created_at']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author_name', 'views', 'likes', 'dislikes', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'description', 'author_name']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['views', 'likes', 'dislikes', 'created_at', 'updated_at']
    inlines = [CommentInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'category')
        }),
        ('Video Details', {
            'fields': ('youtube_url', 'thumbnail')
        }),
        ('Author Information', {
            'fields': ('author', 'author_name', 'author_role', 'author_image')
        }),
        ('Statistics', {
            'fields': ('views', 'likes', 'dislikes', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(VideoProgress)
class VideoProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'video', 'completed', 'watched_at']
    list_filter = ['completed', 'watched_at']
    search_fields = ['user__username', 'video__title']


@admin.register(VideoRating)
class VideoRatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'video', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['user__username', 'video__title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'video', 'text_preview', 'parent', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'video__title', 'text']
    
    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Comment'
