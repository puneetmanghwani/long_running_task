#!/usr/bin/env bash
systemctl restart redis.service
service nginx restart
gunicorn project.wsgi --bind 0.0.0.0:8010 --workers 5 --daemon
celery worker --app=project --loglevel=info

