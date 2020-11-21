from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# setting the default settings of project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# defining project for celery
app = Celery("project",worker_state_db = '/tmp/celery_state')

# defining the namespace
app.config_from_object('django.conf:settings', namespace='CELERY')

# autodiscover tasks in any apps defined in settings.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
	print('Request : {0!r}'.format(self.request))