# EcoDu Development Setup Guide

## Local Development Environment Setup

### Step 1: Install Dependencies

```bash
# Activate virtual environment
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

### Step 2: Install Python Packages

```bash
pip install -r requirements.txt
```

### Step 3: Setup Local Database

```bash
python manage.py migrate
python manage.py createsuperuser
```

### Step 4: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### Step 5: Run Development Server

```bash
python manage.py runserver
```

Then visit: **http://localhost:8000/**

---

## Testing Checklist (Before Deployment)

### 1. Authentication
- [ ] Register new user works
- [ ] Login with credentials works
- [ ] Logout works
- [ ] Profile page loads
- [ ] Edit profile works

### 2. Videos
- [ ] Homepage loads with videos
- [ ] Video detail page loads
- [ ] Video thumbnail displays
- [ ] Like/dislike works (logged in)
- [ ] Search works
- [ ] Category filter works
- [ ] Comments work (logged in)

### 3. Quizzes
- [ ] Quiz loads for video (logged in)
- [ ] Submit answers works
- [ ] Score displays
- [ ] Quiz attempts saved

### 4. Admin Panel
- [ ] Access /admin/ works
- [ ] Add video works
- [ ] Upload thumbnail works
- [ ] Edit video works
- [ ] Delete video works

### 5. Performance
- [ ] Homepage loads in <1s
- [ ] Video detail loads in <500ms
- [ ] No console errors (F12)
- [ ] Images load properly
- [ ] CSS/JS loads properly

### 6. Mobile Responsiveness
- [ ] Test on mobile view (F12)
- [ ] Navigation works on mobile
- [ ] Videos play on mobile
- [ ] Forms work on mobile

---

## Common Issues & Fixes

### Issue: Static files not loading
**Fix:** Run `python manage.py collectstatic --noinput`

### Issue: Media files (thumbnails) not displaying
**Fix:** Ensure `MEDIA_ROOT` and `MEDIA_URL` are correct in settings.py

### Issue: Template not found error
**Fix:** Check `TEMPLATES['DIRS']` in settings.py includes all app template directories

### Issue: 500 error on page load
**Fix:** 
1. Check Django logs: `python manage.py runserver` will show errors
2. Enable DEBUG=True to see detailed error page
3. Check browser console (F12) for JavaScript errors

### Issue: Database errors
**Fix:** Run migrations: `python manage.py migrate`

---

## Deployment Checklist (Before pushing to Railway)

```bash
# 1. Run all tests locally
python manage.py test

# 2. Check for errors
python manage.py check

# 3. Collect static files
python manage.py collectstatic --noinput

# 4. Run migrations
python manage.py migrate

# 5. Run development server and test all features
python manage.py runserver

# 6. After confirming everything works locally:
git add -A
git commit -m "Your message"
git push
```

---

## Project Structure

```
EcoDu/
├── ecodu_project/          # Main Django settings
│   ├── settings.py         # Configuration
│   ├── urls.py             # URL routing
│   └── wsgi.py             # Production WSGI
├── videos/                 # Video app
│   ├── migrations/         # Database migrations
│   ├── templates/          # Video templates
│   ├── views.py           # Video views
│   └── urls.py            # Video URLs
├── users/                  # User authentication app
│   ├── migrations/         # Database migrations
│   ├── templates/          # Auth templates
│   ├── views.py           # Auth views
│   └── urls.py            # Auth URLs
├── quizzes/                # Quiz app
│   ├── migrations/         # Database migrations
│   ├── templates/          # Quiz templates
│   ├── views.py           # Quiz views
│   └── urls.py            # Quiz URLs
├── static/                 # Static files (CSS, JS, images)
│   ├── style.css
│   ├── script.js
│   └── images/
├── media/                  # User uploaded files
│   ├── thumbnails/
│   └── authors/
├── db.sqlite3              # Local development database
├── manage.py               # Django management
├── requirements.txt        # Python dependencies
└── SETUP_GUIDE.md         # This file
```

---

## Environment Variables (Production)

Set these on Railway:

- `DEBUG=False` - Disable debug mode in production
- `SECRET_KEY=your-secret-key` - Set a strong secret key
- `DATABASE_URL=postgresql://...` - Database connection
- `AWS_STORAGE_BUCKET_NAME=ecodu-media` - S3 bucket
- `AWS_ACCESS_KEY_ID=your-access-key`
- `AWS_SECRET_ACCESS_KEY=your-secret-key`
- `AWS_S3_REGION_NAME=us-east-1`

---

## Troubleshooting

### Django won't start
```bash
# Clear cache and reinstall
rm -rf __pycache__
pip install --force-reinstall -r requirements.txt
python manage.py runserver
```

### Database is corrupted
```bash
# Backup old database
mv db.sqlite3 db.sqlite3.backup

# Create fresh database
python manage.py migrate
python manage.py createsuperuser
```

### Port 8000 already in use
```bash
# Use different port
python manage.py runserver 8001
```

### Templates not updating
```bash
# Clear Django cache
python manage.py clear_cache

# Or restart development server
```

---

## Need Help?

Check Django documentation: https://docs.djangoproject.com/
Check error logs in terminal when running `python manage.py runserver`
