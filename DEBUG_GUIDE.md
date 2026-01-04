# EcoDu Debugging Guide

## Quick Debug Commands

### See Database Queries
```python
# In Django shell
python manage.py shell

from django.db import connection
from django.test.utils import CaptureQueriesContext

# Capture all queries
with CaptureQueriesContext(connection) as context:
    # Your code here
    from videos.models import Video
    videos = Video.objects.all()
    
print(f"Total queries: {len(context)}")
for query in context:
    print(query['sql'])
```

### Check for Template Errors
```bash
# Enable detailed error pages
DEBUG = True  # in settings.py

# Run server and check browser console (F12)
python manage.py runserver
```

### Validate Models
```bash
python manage.py check
```

### Test Database Migrations
```bash
python manage.py migrate --plan  # See what will be migrated
python manage.py migrate  # Actually run migrations
```

---

## Common Error Messages & Solutions

### 1. "TemplateDoesNotExist"
**Problem:** Django can't find a template file

**Debug:**
```python
# In settings.py, check TEMPLATES['DIRS']
# Make sure template path is correct:
# Should be: app_name/templates/app_name/template.html

# List all templates:
python manage.py findtemplates
```

**Fix:**
```bash
# Create missing template:
mkdir -p videos/templates/videos/
touch videos/templates/videos/my_template.html
```

---

### 2. "Reverse for 'view_name' not found"
**Problem:** URL pattern doesn't exist

**Debug:**
```python
# Check urls.py for the URL name
# Example: path('video/<slug:slug>/', views.video_detail, name='video_detail')

# Test URL:
python manage.py show_urls
```

**Fix:**
```django
# In template, use correct name:
{% url 'app_name:view_name' %}
```

---

### 3. "No such table: videos_video"
**Problem:** Database table doesn't exist

**Fix:**
```bash
python manage.py migrate
```

---

### 4. "500 Internal Server Error"
**Solution:**
```bash
# 1. Enable DEBUG
DEBUG = True

# 2. Check Django logs
tail -f logs/django.log

# 3. Run in development server to see error
python manage.py runserver

# 4. Check browser console (F12) for JavaScript errors
# 5. Check Network tab to see failed requests
```

---

### 5. "Static files not loading"
**Problem:** CSS/JS/images not loading

**Debug:**
```bash
# Check static files location:
python manage.py findstatic style.css

# Collect static files:
python manage.py collectstatic --noinput

# Check STATIC_URL and STATIC_ROOT in settings
```

**Fix:**
```django
<!-- In templates, use static tag: -->
{% load static %}
<link rel="stylesheet" href="{% static 'style.css' %}">
```

---

### 6. "Media files not loading"
**Problem:** Uploaded images don't display

**Debug:**
```bash
# Check media directory exists:
ls -la media/

# Verify MEDIA_URL and MEDIA_ROOT in settings
```

**Fix in templates:**
```django
<!-- Use .url for media files: -->
<img src="{{ video.thumbnail.url }}" alt="Thumbnail">

<!-- NOT this: -->
<!-- <img src="{% static video.thumbnail %}" alt="Thumbnail"> -->
```

---

## Browser Developer Tools (F12)

### Check for JavaScript Errors
1. Open DevTools: Press `F12`
2. Go to Console tab
3. Look for red error messages
4. Fix JavaScript errors first

### Check Network Issues
1. Go to Network tab
2. Refresh page
3. Look for red failed requests
4. Check response codes:
   - 404 = not found
   - 500 = server error
   - 403 = forbidden

### Check HTML/CSS Issues
1. Go to Elements tab
2. Inspect element
3. Check if classes/IDs are applied correctly

---

## Django Shell for Testing

```bash
python manage.py shell

# Test queries
from videos.models import Video
videos = Video.objects.all()
print(videos)

# Test authentication
from django.contrib.auth import authenticate
user = authenticate(username='admin', password='password123')
print(user)

# Test model methods
video = Video.objects.first()
print(video.get_like_percentage())

# Clear cache
from django.core.cache import cache
cache.clear()
```

---

## Pre-Deployment Checklist

```bash
# 1. Run tests
python manage.py test

# 2. Check for errors
python manage.py check

# 3. Collect static files
python manage.py collectstatic --noinput

# 4. Check migrations
python manage.py migrate

# 5. Run development server
python manage.py runserver

# 6. Test all features locally

# 7. Check logs
tail -f logs/django.log

# 8. Deploy when everything works
git add -A
git commit -m "message"
git push
```

---

## Performance Profiling

### Find Slow Queries
```python
from django.test.utils import override_settings
from django.test import override_settings

@override_settings(DEBUG=True)
def test_performance():
    from django.db import connection
    from django.test.utils import CaptureQueriesContext
    
    with CaptureQueriesContext(connection) as context:
        from videos.models import Video
        videos = list(Video.objects.all())
    
    for query in context:
        print(f"Time: {query['time']}s")
        print(f"SQL: {query['sql']}\n")
```

---

## Production Debugging

### Enable Error Email Notifications
```python
# In settings.py
ADMINS = [('Your Name', 'your-email@example.com')]

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

### View Production Logs
```bash
# On Railway dashboard
# Go to Logs tab to see real-time logs
```

---

## Need More Help?

1. **Django Docs:** https://docs.djangoproject.com/
2. **Stack Overflow:** Search your error message
3. **Django Forum:** https://forum.djangoproject.com/
4. **Debug with pdb:**
   ```python
   import pdb
   pdb.set_trace()  # Execution will pause here
   ```
