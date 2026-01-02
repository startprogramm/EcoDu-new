#!/usr/bin/env bash
# Railway release script - runs AFTER build, when database is available

echo "🗄️ Running database migrations..."
python manage.py migrate --no-input || echo "⚠️  Migrations failed, continuing..."

echo "📝 Populating sample data..."
python manage.py populate_data || echo "⚠️  Data population failed, continuing..."

echo "✅ Release phase completed!"
