# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
from celery import Celery


# Устанавливаем настройки Django для celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailganer.settings')

celery_app = Celery('mailganer')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()



# celery -A mailganer worker -l info