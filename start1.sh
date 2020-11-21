#!/usr/bin/env bash
service redis-server restart
service apache2 restart
gunicorn project.wsgi --bind 0.0.0.0:8000 --workers 4 --daemon
celery -A project worker -l info