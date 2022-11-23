# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
import uuid

from subscriber.models import Subscriber


class MailingList(models.Model):
    """Список рассылок"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32, verbose_name='Название рассылки')
    date_of_completion = models.DateTimeField(default=timezone.now(), blank=False, verbose_name='Дата рассылки')

    def __str__(self):
        return '{name} {date}'.format(name=self.name, date=self.date_of_completion)


class Report(models.Model):
    """Отчет о письмах каждому подписчику каждой рассылки"""
    mailing_list = models.ForeignKey(MailingList, blank=False, on_delete=models.CASCADE, verbose_name='Рассылка')
    subscriber = models.ForeignKey(Subscriber, blank=False, on_delete=models.DO_NOTHING, verbose_name='Получатель')
    sent = models.BooleanField(default=False, blank=False, verbose_name='Письмо отправлено')
    open = models.DateTimeField(default=None, verbose_name='Когда письмо открыто')

    def __str__(self):
        report = 'Получателю ({s}) рассылка {m} отправлена, письмо '.format(s=self.subscriber, m=self.mailing_list.name)
        report += 'не прочитано' if not self.open else 'прочитано {d}'.format(d=self.open)
        return report
