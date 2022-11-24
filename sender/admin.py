# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import MailingList, Report, Sample


class SampleAdmin(admin.ModelAdmin):
    """Регистрация таблицы Списка рассылок в админке"""
    list_display = [field.name for field in Sample._meta.fields]  # Модель в виде таблицы


admin.site.register(Sample, SampleAdmin)  # Регистрируем модель в админке


class MailingListAdmin(admin.ModelAdmin):
    """Регистрация таблицы Списка рассылок в админке"""
    list_display = [field.name for field in MailingList._meta.fields]  # Модель в виде таблицы


admin.site.register(MailingList, MailingListAdmin)  # Регистрируем модель в админке


class ReportAdmin(admin.ModelAdmin):
    """Регистрация таблицы Отчетов о письмах в админке"""
    list_display = [field.name for field in Report._meta.fields]  # Модель в виде таблицы


admin.site.register(Report, ReportAdmin)  # Регистрируем модель в админке
