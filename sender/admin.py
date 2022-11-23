# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import MailingList, Report


# Регистрация таблицы Списка рассылок в админке
class MailingListAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MailingList._meta.fields]  # Модель в виде таблицы


admin.site.register(MailingList, MailingListAdmin)  # Регистрируем модель в админке


# Регистрация таблицы Отчетов о письмах в админке
class ReportAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Report._meta.fields]  # Модель в виде таблицы


admin.site.register(Report, ReportAdmin)  # Регистрируем модель в админке
