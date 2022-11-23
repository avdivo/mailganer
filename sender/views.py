# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def mailing_list_page(request):
    """Вывод страницы со списком рассылок отсортированных по дате и кнопкой добавления новой рассылки"""
    return render(request, 'mailing_list.html', locals())


def new_list(request):
    """Вывод формы для создания новой рассылки"""
    return render(request, 'new_list.html', locals())
