# -*- coding: utf-8 -*-
import time
import datetime

from .celery import celery_app

from subscriber.models import Subscriber


@celery_app.task
def send_mail(id, sample):
    subscriber = Subscriber.objects.values().get(id=id)  # Запрос данных получателя
    print("Hello", subscriber['first_name'], subscriber['last_name'], "you have a mail in sample", sample)
