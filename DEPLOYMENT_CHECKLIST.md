# Pre-Deployment Checklist

Use this checklist before deploying to production to ensure everything is configured correctly.

## Code & Configuration

- [ ] All changes committed to Git
- [ ] `.env` file is NOT committed (check `.gitignore`)
- [ ] `requirements.txt` includes all dependencies
- [ ] `settings.py` uses environment variables for sensitive data
- [ ] `DEBUG=False` in production environment variables
- [ ] `ALLOWED_HOSTS` configured for production domain
- [ ] `SECRET_KEY` is unique and secure (not the default)

## Database

- [ ] PostgreSQL database created on hosting platform
- [ ] `DATABASE_URL` environment variable set
- [ ] Database migrations ready to run
- [ ] Plan for initial data/superuser creation

## Static Files

- [ ] `STATIC_ROOT` configured in settings
- [ ] WhiteNoise middleware installed and configured
- [ ] `collectstatic` command in build script

## Security

- [ ] HTTPS enabled (automatic on Railway/Render)
- [ ] Security headers configured (in `settings.py`)
- [ ] CSRF protection enabled
- [ ] Session cookies secure

## Environment Variables

Required variables set on hosting platform:

- [ ] `SECRET_KEY` - Generated unique key
- [ ] `DEBUG` - Set to `False`
- [ ] `ALLOWED_HOSTS` - Your production domain
- [ ] `DATABASE_URL` - Set automatically by platform

## Testing

- [ ] Application runs locally with production settings
- [ ] All pages load correctly
- [ ] Admin panel accessible
- [ ] User authentication works
- [ ] Video playback functional
- [ ] Quiz system operational

## Deployment Platform Setup

### For Render:
- [ ] GitHub repository connected
- [ ] PostgreSQL database created
- [ ] Web service configured
- [ ] Build command: `./build.sh`
- [ ] Start command: `gunicorn ecodu_project.wsgi:application`
- [ ] Environment variables set

### For Railway:
- [ ] GitHub repository connected
- [ ] PostgreSQL plugin added
- [ ] Build command configured
- [ ] Start command configured
- [ ] Environment variables set

## Post-Deployment

- [ ] Application accessible at production URL
- [ ] Create superuser account
- [ ] Test admin panel login
- [ ] Upload initial content (videos, quizzes)
- [ ] Test all major features
- [ ] Monitor logs for errors
- [ ] Set up custom domain (optional)

## Monitoring

- [ ] Check deployment logs
- [ ] Monitor application performance
- [ ] Set up error tracking (optional)
- [ ] Configure backups (optional)

## Documentation

- [ ] Team knows how to deploy updates
- [ ] Environment variables documented
- [ ] Deployment process documented
- [ ] Troubleshooting guide available

---

## Quick Commands Reference

**Generate SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Create Superuser (after deployment):**
```bash
python create_superuser.py
# or
python manage.py createsuperuser
```

**Collect Static Files (local test):**
```bash
python manage.py collectstatic --no-input
```

**Run Migrations (local test):**
```bash
python manage.py migrate
```

**Test Production Settings Locally:**
```bash
# Set environment variables first
export DEBUG=False
export SECRET_KEY=your-secret-key
export ALLOWED_HOSTS=localhost,127.0.0.1
python manage.py runserver
```
