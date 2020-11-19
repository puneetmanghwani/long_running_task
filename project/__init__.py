
# importing these so that celery app is imported always at django startup for shared tasks.

from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app

