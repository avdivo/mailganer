# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import uuid


class Group(models.Model):
    """Группы получателей, рассылка делается для группы. Письма отправляются получателям
    которые входят в группу. Получатель может состоять в нескольких группах.
    """
    group = models.CharField(max_length=32, verbose_name='Группа')

    def __unicode__(self):
        return self.group


class Subscriber(models.Model):
    """Получатели рассылок
    Поле "group" включено для разделения получателей на группы и в случае необходисости
    может стать связью many_to_many с таблицей групп"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=64, verbose_name='Имя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия')
    email = models.CharField(max_length=128, verbose_name='Email')
    birthday = models.CharField(max_length=10, verbose_name='Дата рождения')
    group = models.ManyToManyField(Group, verbose_name='Группы')

    def __unicode__(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)
