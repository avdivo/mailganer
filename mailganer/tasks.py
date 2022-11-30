# -*- coding: utf-8 -*-
import datetime

from django.template.loader import get_template
from .celery import celery_app

from subscriber.models import Subscriber
from sender.models import MailingList, Report
from .utils import send_email


@celery_app.task
def send_mail(subscriber_id, list_id, site_url):
    """Задание для Celery для отправки письма получателю с заданным id и по заданному шаблону"""
    subscriber = Subscriber.objects.get(id=subscriber_id)  # Запрос данных получателя
    new_list = MailingList.objects.get(id=list_id)  # Запрос данных рассылки

    new_report = Report.objects.create(mailing_list=new_list, subscriber=subscriber)

    # Подготовка данных для письма.
    # Расширение таблиц получателей, рассылок, шаблонов, а так же добавление логики в этой функции
    # позволит увеличить возможности программы. Например, изменить наборы данных в зависимости от шаблона.
    for_mail = dict()
    for_mail['first_name'] = subscriber.first_name
    for_mail['last_name'] = subscriber.last_name
    for_mail['deadline'] = new_list.date_of_completion + datetime.timedelta(days=7)
    for_mail['open'] = new_list.id
    sample = 'samples/' + new_list.sample.sample

    message = get_template(sample).render(locals())  # Создаем html сообщение из шаблона
    is_email = send_email(message, [subscriber.email])  # Отправляем письмо и получаем успешность
    if is_email:
        # Если письмо отп   равлено успешно
        print('--------------------------- Письмо отправлено успешно ------------------------------')
        new_report.sent = True  # Подтверждение отправки письма
        new_report.save()
    else:
        print('--------------------------- Письмо не отправлено ------------------------------')
