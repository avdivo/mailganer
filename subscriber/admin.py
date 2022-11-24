# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Subscriber, Group


class SubscriberAdmin(admin.ModelAdmin):
    """Регистрация таблицы получатели в админке"""
    list_display = [field.name for field in Subscriber._meta.fields]  # Модель в виде таблицы


admin.site.register(Subscriber, SubscriberAdmin)  # Регистрируем модель в админке


class GroupAdmin(admin.ModelAdmin):
    """Регистрация таблицы Группы в админке"""
    list_display = [field.name for field in Group._meta.fields]  # Модель в виде таблицы


admin.site.register(Group, GroupAdmin)  # Регистрируем модель в админке
