import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecodu_project.settings')
django.setup()

from users.models import CustomUser

# Create superuser if it doesn't exist
if not CustomUser.objects.filter(username='admin').exists():
    CustomUser.objects.create_superuser(
        username='admin',
        email='admin@ecodu.com',
        password='admin123',
        first_name='Admin',
        last_name='User'
    )
    print("Superuser created successfully!")
    print("Username: admin")
    print("Password: admin123")
else:
    print("Superuser already exists!")
