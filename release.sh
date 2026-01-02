#!/usr/bin/env bash
# Railway release script - runs AFTER build, when database is available

echo "🗄️ Running database migrations..."
python manage.py migrate --no-input

echo "✅ Release phase completed!"
