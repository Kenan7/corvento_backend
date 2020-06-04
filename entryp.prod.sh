#!/bin/sh

echo "✨ migrate"
python manage.py migrate --no-input

echo "🎅 collectstatic"
python manage.py collectstatic --no-input


# if [ "$DATABASE" = "postgres" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -z $SQL_HOST $SQL_PORT; do
#       sleep 0.1
#     done

#     echo "PostgreSQL started"
# fi

# exec "$@"