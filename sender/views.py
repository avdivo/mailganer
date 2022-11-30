# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils import timezone

from django.conf import settings
from .forms import NewListForm
from .models import MailingList
from sender.models import Report
from .services import send_group, set_tzname


def mailing_list_page(request):
    """Вывод страницы со списком рассылок отсортированных по дате и кнопкой добавления новой рассылки"""

    # Установка часового пояса
    tzname = set_tzname(request)

    mailing_list = MailingList.objects.order_by('-date_of_completion')  # Чтение списка рассылок
    # Подготовка словаря для вывода таблицы рассылок
    now_datetime = timezone.now()
    table = []  # Данные в шаблон
    string = dict()
    for mailing in mailing_list:
        string['id'] = mailing.id
        string['name'] = mailing.name
        string['group'] = mailing.group
        string['sample'] = mailing.sample
        string['date'] = mailing.date_of_completion
        string['status'] = 'Ожидание' if string['date'] > now_datetime else 'Ok'
        table.append(string)
        string = dict()
    return render(request, 'mailing_list.html', locals())


def new_list(request):
    """Вывод формы для создания новой рассылки"""
    if request.method == 'POST':
        # Получены данные для создания новой рассылки
        form = NewListForm(request.POST)
        site_url = request.META['HTTP_HOST']
        if form.is_valid():
            send_group(form.save(commit=True), site_url)
            return HttpResponseRedirect('list')
    else:
        form = NewListForm()
    return render(request, 'new_list.html', {'form': form})


def report(request, list_id):
    """Отчет о рассылке с номером полученным в адресной строке"""
    ml = MailingList.objects.get(id=list_id)
    table = Report.objects.filter(mailing_list=ml)
    return render(request, 'mailing_report.html', locals())


def open_mail(request, report_id):
    """Подтверждение открытия письма клиентом
    Открытие письма потребует загрузки изображения, которая будет приводить к открытию этой функции"""
    image = open(os.path.join(settings.STATIC_ROOT, 'img/pixel.png'), 'rb')
    reports = Report.objects.get(id=report_id)
    reports.open = timezone.now()
    reports.save()
    return HttpResponse(image.read(), status=201)
