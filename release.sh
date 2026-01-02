#!/usr/bin/env bash
# Railway release script - runs AFTER build, when database is available

set -o errexit

echo "🗄️ Running database migrations..."
python manage.py migrate --no-input

echo "📝 Populating sample data..."
python populate_data.py

echo "✅ Release phase completed!"
