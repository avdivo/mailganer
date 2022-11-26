# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NewListForm
from .services import send_group


def mailing_list_page(request):
    """Вывод страницы со списком рассылок отсортированных по дате и кнопкой добавления новой рассылки"""
    return render(request, 'mailing_list.html', locals())


def new_list(request):
    """Вывод формы для создания новой рассылки"""
    if request.method == 'POST':
        # Получены данные для создания новой рассылки
        form = NewListForm(request.POST)
        if form.is_valid():
            send_group(form.save(commit=True))
            return HttpResponseRedirect('list')
    else:
        form = NewListForm()
    return render(request, 'new_list.html', {'form': form})
