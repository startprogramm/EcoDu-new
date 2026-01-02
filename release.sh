#!/usr/bin/env bash
# Railway release script - runs AFTER build, when database is available

echo "🗄️ Running database migrations..."
python manage.py migrate --no-input

echo "👤 Creating admin user..."
python manage.py shell << END
from users.models import CustomUser
if not CustomUser.objects.filter(username='admin').exists():
    CustomUser.objects.create_superuser(
        username='admin',
        email='admin@ecodu.com',
        password='admin123',
        first_name='Admin',
        last_name='User'
    )
    print("✅ Admin user created: admin / admin123")
else:
    print("ℹ️  Admin user already exists")
END

echo "✅ Release phase completed!"
