# Django Templates Best Practices

## ✅ DO: Proper Template Structure

### 1. Use Static Files (CSS, JS, Images)
```django
{% load static %}
<link rel="stylesheet" href="{% static 'style.css' %}">
<script src="{% static 'script.js' %}"></script>
<img src="{% static 'logo.png' %}" alt="Logo">
```

### 2. Use Media Files (User Uploads)
```django
<!-- For uploaded files ONLY -->
<img src="{{ video.thumbnail.url }}" alt="Thumbnail">
<img src="{{ user.avatar.url }}" alt="Avatar">
```

### 3. Use URL Tags
```django
<!-- Good: Django generates correct URL -->
<a href="{% url 'app_name:view_name' %}">Link</a>
<a href="{% url 'videos:video_detail' video.slug %}">Video</a>

<!-- Bad: Hardcoded URLs - breaks if you change routing -->
<a href="/videos/my-video/">Video</a>
```

### 4. Use Template Tags for Logic
```django
<!-- Good: Use template tags -->
{% if user.is_authenticated %}
    <p>Hello, {{ user.username }}!</p>
{% else %}
    <p>Please login</p>
{% endif %}

<!-- Use filters -->
{{ text|truncatewords:20 }}
{{ date|date:"Y-m-d" }}
{{ value|default:"N/A" }}

<!-- Use template tags -->
{% for video in videos %}
    <h3>{{ video.title }}</h3>
{% empty %}
    <p>No videos found</p>
{% endfor %}
```

### 5. Optimize Database Queries
```django
<!-- In views.py, use select_related for ForeignKey -->
videos = Video.objects.select_related('category', 'author')

<!-- In views.py, use prefetch_related for ManyToMany/Reverse FK -->
videos = Video.objects.prefetch_related('comments')

<!-- Then in template, no N+1 queries -->
{% for video in videos %}
    <p>Category: {{ video.category.name }}</p>
    <p>Author: {{ video.author.username }}</p>
{% endfor %}
```

### 6. Use Template Inheritance
```django
<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Default Title{% endblock %}</title>
</head>
<body>
    <header>EcoDu</header>
    {% block content %}{% endblock %}
    <footer>Copyright 2025</footer>
</body>
</html>

<!-- other_page.html -->
{% extends "base.html" %}

{% block title %}Video Details{% endblock %}

{% block content %}
    <h1>{{ video.title }}</h1>
{% endblock %}
```

### 7. Handle Missing Data Gracefully
```django
<!-- Good: Check if data exists before using -->
{% if video.thumbnail %}
    <img src="{{ video.thumbnail.url }}" alt="{{ video.title }}">
{% else %}
    <img src="{% static 'placeholder.png' %}" alt="No thumbnail">
{% endif %}

<!-- Use default filter -->
<p>Description: {{ video.description|default:"No description" }}</p>
```

---

## ❌ DON'T: Common Mistakes

### 1. ❌ Mix Static and Media Files
```django
<!-- WRONG -->
<img src="{% static video.thumbnail %}">

<!-- RIGHT -->
<img src="{{ video.thumbnail.url }}">
```

### 2. ❌ Hardcode URLs
```django
<!-- WRONG -->
<a href="/users/login/">Login</a>

<!-- RIGHT -->
<a href="{% url 'users:login' %}">Login</a>
```

### 3. ❌ Use JavaScript to Navigate
```javascript
// WRONG - Prevents normal link behavior
link.addEventListener('click', () => {
    location.href = '/new-page/';
});

// RIGHT - Let links work normally
// If you need to do something, prevent default only for that action
link.addEventListener('click', (e) => {
    if (needsSpecialHandling) {
        e.preventDefault();
        // Do something special
    }
});
```

### 4. ❌ Put Logic in Templates
```django
<!-- WRONG - Complex logic in template -->
{% if user.profile.videos_watched > 10 and user.is_authenticated and user.profile.badge_level > 2 %}
    <span>Gold Member</span>
{% endif %}

<!-- RIGHT - Put logic in view -->
<!-- In views.py -->
context['is_gold_member'] = (
    user.profile.videos_watched > 10 and 
    user.profile.badge_level > 2
)

<!-- In template -->
{% if is_gold_member %}
    <span>Gold Member</span>
{% endif %}
```

### 5. ❌ N+1 Query Problem
```django
<!-- In views.py - WRONG -->
videos = Video.objects.all()  # 1 query
# Then in template:
{% for video in videos %}
    {{ video.category.name }}  <!-- 1 query per video! N+1 problem -->
{% endfor %}

<!-- CORRECT -->
videos = Video.objects.select_related('category')  # 1 query with join
{% for video in videos %}
    {{ video.category.name }}  <!-- No extra queries -->
{% endfor %}
```

### 6. ❌ Display Invalid Data
```django
<!-- WRONG - Can crash if thumbnail is None -->
<img src="{{ video.thumbnail }}" alt="Thumbnail">

<!-- RIGHT -->
{% if video.thumbnail %}
    <img src="{{ video.thumbnail.url }}" alt="Thumbnail">
{% endif %}
```

---

## Template Checklist

Before deploying, check:

- [ ] All static files use `{% static %}`
- [ ] All media files use `.url` property
- [ ] All links use `{% url %}`
- [ ] All templates extend base.html (or have proper structure)
- [ ] All data has null/empty checks
- [ ] No N+1 query problems (use select_related/prefetch_related)
- [ ] Error messages are user-friendly
- [ ] Mobile responsive design works
- [ ] Forms have CSRF token: `{% csrf_token %}`
- [ ] No hardcoded paths or URLs
- [ ] No complex logic in templates
- [ ] Test with DEBUG=False locally

---

## Common Template Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `TemplateDoesNotExist` | Template file not found | Check file path: `app/templates/app/template.html` |
| `Could not resolve image URL for field` | Using `{% static %}` for uploads | Use `{{ field.url }}` instead |
| `Reverse for 'name' not found` | URL pattern name doesn't exist | Check `urls.py` for correct name |
| `No image showing` | Wrong file path | Check if file exists, use browser DevTools |
| `Page looks broken` | Missing CSS/JS files | Run `python manage.py collectstatic` |
| `Form not working` | Missing CSRF token | Add `{% csrf_token %}` inside `<form>` |

---

## Tips & Tricks

### Debugging Template Variables
```django
<!-- See what's available -->
{{ debug_variables }}

<!-- Or use Django Debug Toolbar -->
<!-- Install: pip install django-debug-toolbar -->
```

### Conditional CSS Classes
```django
<div class="video {% if video.featured %}featured{% endif %}">
    {{ video.title }}
</div>
```

### Loop Information
```django
{% for video in videos %}
    <div>
        {% if forloop.first %}
            <h2>First Video</h2>
        {% endif %}
        
        {{ video.title }}
        
        {% if forloop.last %}
            <p>That's all!</p>
        {% endif %}
    </div>
{% endfor %}
```

### Date Formatting
```django
{{ video.created_at|date:"F d, Y" }}  <!-- January 01, 2025 -->
{{ video.created_at|date:"H:i" }}  <!-- 14:30 -->
{{ video.created_at|timesince }}  <!-- 2 days ago -->
```

### Text Formatting
```django
{{ text|upper }}  <!-- UPPERCASE -->
{{ text|lower }}  <!-- lowercase -->
{{ text|title }}  <!-- Title Case -->
{{ text|truncatewords:10 }}  <!-- First 10 words... -->
{{ text|slugify }}  <!-- text-version -->
```
