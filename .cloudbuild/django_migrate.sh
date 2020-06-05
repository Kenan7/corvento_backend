#!/bin/sh

echo "✨ migrate"
python manage.py migrate --no-input
