# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Subscriber


# Регистрация таблицы получатели в админке
class SubscriberAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subscriber._meta.fields]  # Модель в виде таблицы


admin.site.register(Subscriber, SubscriberAdmin)  # Регистрируем модель в админке