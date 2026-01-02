#!/usr/bin/env bash
# Railway release script - runs AFTER build, when database is available

set -o errexit

echo "🗄️ Running database migrations..."
python manage.py migrate --no-input

echo "📝 Populating sample data..."
python manage.py populate_data

echo "✅ Release phase completed!"
