# Deploying EcoDu to Render.com

This guide will walk you through deploying your EcoDu application to Render.com for testing.

## Prerequisites

- GitHub account with your EcoDu repository
- Render.com account (free tier available)

## Step 1: Prepare Your Repository

1. **Commit all changes** to your GitHub repository:
   ```bash
   git add .
   git commit -m "Prepare for production deployment"
   git push origin main
   ```

## Step 2: Create a Render Account

1. Go to [render.com](https://render.com)
2. Sign up using your GitHub account
3. Authorize Render to access your repositories

## Step 3: Create a PostgreSQL Database

1. From your Render dashboard, click **"New +"** → **"PostgreSQL"**
2. Configure the database:
   - **Name**: `ecodu-db`
   - **Database**: `ecodu_db`
   - **User**: `ecodu_user`
   - **Region**: Choose closest to your users
   - **Plan**: Free
3. Click **"Create Database"**
4. **Important**: Copy the **Internal Database URL** (starts with `postgresql://`)

## Step 4: Create a Web Service

1. From your Render dashboard, click **"New +"** → **"Web Service"**
2. Connect your GitHub repository
3. Configure the service:

   **Basic Settings:**
   - **Name**: `ecodu-test`
   - **Region**: Same as your database
   - **Branch**: `main`
   - **Root Directory**: Leave empty
   - **Runtime**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn ecodu_project.wsgi:application --bind 0.0.0.0:$PORT`

   **Plan:**
   - Select **Free** tier

4. Click **"Advanced"** to add environment variables

## Step 5: Configure Environment Variables

Add these environment variables (click **"Add Environment Variable"** for each):

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Generate using: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `ecodu-test.onrender.com` (use your actual Render URL) |
| `DATABASE_URL` | Paste the Internal Database URL from Step 3 |

## Step 6: Deploy

1. Click **"Create Web Service"**
2. Render will automatically:
   - Clone your repository
   - Install dependencies
   - Collect static files
   - Run migrations
   - Start your application

3. Monitor the deployment logs for any errors

## Step 7: Create Superuser

After successful deployment:

1. Go to your service's **"Shell"** tab
2. Run:
   ```bash
   python create_superuser.py
   ```
   Or manually:
   ```bash
   python manage.py createsuperuser
   ```

## Step 8: Access Your Application

1. Your app will be available at: `https://ecodu-test.onrender.com`
2. Admin panel: `https://ecodu-test.onrender.com/admin/`

## Troubleshooting

### Build Fails
- Check the build logs in Render dashboard
- Ensure `build.sh` has correct permissions
- Verify all dependencies are in `requirements.txt`

### Static Files Not Loading
- Check that `STATIC_ROOT` is set correctly
- Verify WhiteNoise is in `MIDDLEWARE`
- Run `python manage.py collectstatic` in Shell

### Database Connection Errors
- Verify `DATABASE_URL` is set correctly
- Ensure database and web service are in same region
- Check database is running in Render dashboard

### 500 Internal Server Error
- Check logs in Render dashboard
- Verify `DEBUG=False` and `ALLOWED_HOSTS` is set
- Ensure migrations have run successfully

## Updating Your Application

To deploy updates:

1. Push changes to GitHub:
   ```bash
   git add .
   git commit -m "Your update message"
   git push origin main
   ```

2. Render will automatically detect changes and redeploy

## Free Tier Limitations

- Web service spins down after 15 minutes of inactivity
- First request after spin-down may take 30-60 seconds
- Database limited to 90 days on free tier
- 750 hours/month of runtime

## Next Steps

Once testing is complete on Render, you can deploy to Railway for production using the Railway deployment guide.
