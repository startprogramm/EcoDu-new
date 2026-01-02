# Deploying EcoDu to Railway.app

This guide will walk you through deploying your EcoDu application to Railway.app for production.

## Prerequisites

- GitHub account with your EcoDu repository
- Railway account (free tier available with $5 credit)

## Step 1: Prepare Your Repository

1. **Commit all changes** to your GitHub repository:
   ```bash
   git add .
   git commit -m "Prepare for Railway production deployment"
   git push origin main
   ```

## Step 2: Create a Railway Account

1. Go to [railway.app](https://railway.app)
2. Sign up using your GitHub account
3. You'll receive $5 in free credits (no credit card required initially)

## Step 3: Create a New Project

1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose your **EcoDu** repository
4. Railway will automatically detect it's a Django application

## Step 4: Add PostgreSQL Database

1. In your project dashboard, click **"New"** → **"Database"** → **"Add PostgreSQL"**
2. Railway will automatically:
   - Create a PostgreSQL database
   - Generate a `DATABASE_URL` environment variable
   - Link it to your web service

## Step 5: Configure Environment Variables

1. Click on your web service (not the database)
2. Go to **"Variables"** tab
3. Click **"New Variable"** and add these:

| Variable | Value |
|----------|-------|
| `SECRET_KEY` | Generate using: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | Leave empty initially, Railway will set this automatically |

**Note**: `DATABASE_URL` is automatically set by Railway when you add PostgreSQL.

## Step 6: Configure Build and Start Commands

1. In your service, go to **"Settings"** tab
2. Scroll to **"Deploy"** section:

   **Build Command:**
   ```bash
   pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate
   ```

   **Start Command:**
   ```bash
   gunicorn ecodu_project.wsgi:application
   ```

3. Click **"Save"**

## Step 7: Configure Allowed Hosts

1. After first deployment, Railway will assign you a URL like: `ecodu-production.up.railway.app`
2. Go back to **"Variables"** tab
3. Update `ALLOWED_HOSTS`:
   ```
   ecodu-production.up.railway.app
   ```
   (Replace with your actual Railway domain)

## Step 8: Deploy

1. Railway automatically deploys when you push to GitHub
2. For manual deployment, click **"Deploy"** in the dashboard
3. Monitor deployment logs in the **"Deployments"** tab

## Step 9: Create Superuser

1. In your service dashboard, click **"Settings"**
2. Scroll to **"Service"** section
3. Click **"Open Shell"** or use Railway CLI:
   ```bash
   railway run python create_superuser.py
   ```
   Or manually:
   ```bash
   railway run python manage.py createsuperuser
   ```

## Step 10: Access Your Application

1. Your app will be available at your Railway URL
2. Admin panel: `https://your-app.up.railway.app/admin/`

## Custom Domain (Optional)

1. In your service, go to **"Settings"** → **"Domains"**
2. Click **"Custom Domain"**
3. Add your domain (e.g., `ecodu.com`)
4. Update your DNS records as instructed
5. Update `ALLOWED_HOSTS` environment variable to include your custom domain

## Monitoring and Logs

1. **Logs**: Click on your service → **"Logs"** tab
2. **Metrics**: View CPU, memory, and network usage
3. **Deployments**: See deployment history and rollback if needed

## Automatic Deployments

Railway automatically deploys when you push to your main branch:

```bash
git add .
git commit -m "Update application"
git push origin main
```

Railway will:
1. Detect the push
2. Run build commands
3. Collect static files
4. Run migrations
5. Deploy new version

## Environment Management

### Development vs Production

You can create multiple environments:

1. Create a new service for staging: **"New"** → **"GitHub Repo"**
2. Use different branch (e.g., `develop`)
3. Set `DEBUG=True` for staging
4. Keep production with `DEBUG=False`

## Pricing

- **Free Tier**: $5 credit/month (no credit card required)
- **Hobby Plan**: $5/month (includes $5 credit)
- **Pro Plan**: $20/month (includes $20 credit)

Usage is based on:
- CPU time
- Memory usage
- Network egress
- Database storage

## Troubleshooting

### Build Fails
- Check deployment logs
- Verify `requirements.txt` has all dependencies
- Ensure Python version matches `runtime.txt`

### Database Connection Issues
- Verify PostgreSQL service is running
- Check `DATABASE_URL` is set automatically
- Ensure web service and database are in same project

### Static Files Not Loading
- Verify `collectstatic` runs in build command
- Check WhiteNoise configuration in `settings.py`
- Ensure `STATIC_ROOT` is set correctly

### Application Crashes
- Check logs for error messages
- Verify all environment variables are set
- Ensure migrations have run successfully

## Backup Database

1. Install Railway CLI:
   ```bash
   npm install -g @railway/cli
   ```

2. Login:
   ```bash
   railway login
   ```

3. Link to your project:
   ```bash
   railway link
   ```

4. Backup database:
   ```bash
   railway run pg_dump $DATABASE_URL > backup.sql
   ```

## Scaling

Railway automatically scales based on usage. For manual scaling:

1. Go to **"Settings"** → **"Resources"**
2. Adjust memory and CPU limits
3. Note: Higher resources = higher costs

## Support

- [Railway Documentation](https://docs.railway.app)
- [Railway Discord](https://discord.gg/railway)
- [Railway Status](https://status.railway.app)

## Next Steps

1. Set up custom domain
2. Configure email service (for password resets, notifications)
3. Set up monitoring and alerts
4. Configure automated backups
5. Add CI/CD pipeline for testing before deployment
