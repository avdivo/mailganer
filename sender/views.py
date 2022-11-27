# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from .forms import NewListForm
from .models import MailingList
from .services import send_group, set_tzname


def mailing_list_page(request):
    """Вывод страницы со списком рассылок отсортированных по дате и кнопкой добавления новой рассылки"""

    # Установка часового пояса
    tzname = set_tzname(request)

    mailing_list = MailingList.objects.order_by('date_of_completion')  # Чтение списка рассылок
    # Подготовка словаря для вывода таблицы рассылок
    now_datetime = timezone.now()
    table = []
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
        if form.is_valid():
            send_group(form.save(commit=True))
            # send_group()
            return HttpResponseRedirect('list')
    else:
        form = NewListForm()
    return render(request, 'new_list.html', {'form': form})
