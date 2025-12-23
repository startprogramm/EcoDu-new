from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Custom admin for user management"""
    list_display = ['username', 'email', 'first_name', 'last_name', 'total_points', 'videos_watched', 'is_staff']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'created_at']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['-created_at']
    
    fieldsets = UserAdmin.fieldsets + (
        ('EcoDu Profile', {'fields': ('avatar', 'bio', 'total_points', 'videos_watched', 'quizzes_passed')}),
    )
