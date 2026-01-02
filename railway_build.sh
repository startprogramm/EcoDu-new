#!/usr/bin/env bash
# Railway.app build script

set -o errexit  # Exit on error

echo "🔧 Installing dependencies..."
pip install -r requirements.txt

echo "📦 Collecting static files..."
python manage.py collectstatic --no-input --clear

echo "🗄️ Running database migrations..."
python manage.py migrate --no-input

echo "✅ Build completed successfully!"
