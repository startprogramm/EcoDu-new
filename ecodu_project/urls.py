"""
URL configuration for ecodu_project project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('videos.urls')),
    path('users/', include('users.urls')),
    path('quizzes/', include('quizzes.urls')),
]

# Serve media files (important for admin uploads)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Serve static files in development only; production uses WhiteNoise
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

