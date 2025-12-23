# EcoDu - Environmental Education Platform

A full-stack Django web application for environmental education with video lessons, interactive quizzes, and user progress tracking.

## Features

- 🎥 Video lessons organized by categories
- 📝 Interactive quizzes with scoring
- 👤 User authentication and profiles
- 💬 Comments and discussions
- 📊 Progress tracking and analytics
- 🏆 Leaderboards and achievements
- 🎨 Beautiful, responsive UI

## Tech Stack

- **Backend**: Django 6.0
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Bootstrap 5 with custom CSS

## Local Development

### Prerequisites
- Python 3.14+
- Git

### Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd EcoDu
```

2. Create virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python create_superuser.py
# Or manually: python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

7. Access the application:
- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/
- Login: admin / admin123

## Deployment

This project is ready to deploy on:
- Railway.app (recommended)
- Render.com
- Heroku
- PythonAnywhere

See deployment documentation for platform-specific instructions.

## Project Structure

```
EcoDu/
├── ecodu_project/      # Django project settings
├── videos/             # Video management app
├── users/              # User authentication app
├── quizzes/            # Quiz system app
├── static/             # Static files (CSS, JS, images)
├── media/              # User uploads
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## Admin Panel

Access the admin panel at `/admin/` to:
- Manage videos and categories
- Create and edit quizzes
- View user statistics
- Moderate comments

## License

© 2025 EcoDu. All rights reserved.
