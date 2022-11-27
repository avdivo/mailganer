# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
import uuid

from subscriber.models import Subscriber, Group


class Sample(models.Model):
    """Шаблоны писем. Имена файлов *.html в папке templates/amples
    Регистрируются пользователем через админку при добавлении нового шаблона в папку.
    Возможно добавление функционала для автоматической загрузки шаблонов и регистрации.
    """
    sample = models.CharField(max_length=32, verbose_name='Шаблон письма')

    def __unicode__(self):
        return self.sample


class MailingList(models.Model):
    """Список рассылок"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32, verbose_name='Название рассылки')
    date_of_completion = models.DateTimeField(default=timezone.now(), blank=False, verbose_name='Дата рассылки')
    group = models.ForeignKey(Group, blank=False, default=0, on_delete=models.DO_NOTHING, verbose_name='Группа получателей')
    sample = models.ForeignKey(Sample, blank=False, default=0, on_delete=models.DO_NOTHING, verbose_name='Шаблон письма')


class Report(models.Model):
    """Отчет о письмах каждому подписчику каждой рассылки"""
    mailing_list = models.ForeignKey(MailingList, blank=False, on_delete=models.CASCADE, verbose_name='Рассылка')
    subscriber = models.ForeignKey(Subscriber, blank=False, on_delete=models.DO_NOTHING, verbose_name='Получатель')
    sent = models.BooleanField(default=False, blank=False, verbose_name='Письмо отправлено')
    open = models.DateTimeField(default=None, verbose_name='Когда письмо открыто')

    def __unicode__(self):
        report = 'Получателю ({s}) рассылка {m} отправлена, письмо '.format(s=self.subscriber, m=self.mailing_list.name)
        report += 'не прочитано' if not self.open else 'прочитано {d}'.format(d=self.open)
        return report
