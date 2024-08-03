#!/bin/sh
set -e

if [ "$BACKUP_ENABLE" = "TRUE" ]; then
  python .venv/bin/supervisord -c supervisord.conf
fi

cd pdfding

if [ "$DATABASE_TYPE" = "POSTGRES" ]
then
    POSTGRES_PORT="${POSTGRES_PORT:-5432}"
    echo "Waiting for postgres..."

    while ! nc -z postgres $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

HOST_PORT="${HOST_PORT:-8000}"

python manage.py migrate
python -m gunicorn --bind 0.0.0.0:$HOST_PORT --workers 3 core.wsgi:application
