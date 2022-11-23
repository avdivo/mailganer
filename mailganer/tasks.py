from .celery import celery_app
import time
import datetime


@celery_app.task
def send_report(n):
    time.sleep(2)
    now = datetime.datetime.now()
    print("---- ", n, now.second)
