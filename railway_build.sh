#!/usr/bin/env bash
# Railway.app build script

set -o errexit  # Exit on error

echo "🔧 Installing dependencies..."
pip install -r requirements.txt

echo "📦 Collecting static files..."
python manage.py collectstatic --no-input --clear

echo "✅ Build completed successfully!"
echo "ℹ️  Note: Migrations will run automatically when the app starts"
