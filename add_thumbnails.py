"""
Script to add thumbnails to videos
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecodu_project.settings')
django.setup()

from videos.models import Video

# Map video titles to their thumbnail images
thumbnails = {
    'Yovvoyi tabiat': 'yovvoyitabiat.jpg',
    "O'rmonlar yo'qolishi": "o'rmonlar.jpg",
    'Suv ifloslanishi': 'suv.png',
    'Havo ifloslanishi': 'havo.jpg',
    'Plastik ifloslanish': 'plastik.jpg',
}

print("Adding thumbnails to videos...")
for title, thumbnail in thumbnails.items():
    try:
        video = Video.objects.get(title=title)
        video.thumbnail = thumbnail
        video.save()
        print(f"OK: {title} -> {thumbnail}")
    except Video.DoesNotExist:
        print(f"ERROR: Video not found: {title}")

print("\nDone! All videos now have unique thumbnails.")
