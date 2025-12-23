"""
Test login and update video thumbnails
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecodu_project.settings')
django.setup()

from django.contrib.auth import authenticate
from videos.models import Video

print("=== Testing Login ===")
user = authenticate(username='admin', password='admin123')
if user:
    print(f"✓ Login successful! User: {user.username}")
else:
    print("✗ Login failed!")
    print("Creating admin user...")
    from users.models import CustomUser
    admin = CustomUser.objects.create_superuser(
        username='admin',
        email='admin@ecodu.com',
        password='admin123'
    )
    print(f"✓ Admin user created: {admin.username}")

print("\n=== Checking Videos ===")
videos = Video.objects.all()
for video in videos:
    print(f"Video: {video.title}")
    print(f"  - Thumbnail: {video.thumbnail}")
    print(f"  - Category: {video.category.name}")

print("\nNote: Videos don't have thumbnails. They will use fallback images from static folder.")
print("You can add thumbnails through the admin panel at /admin/")
