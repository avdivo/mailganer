# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
import pytz
from django.utils import timezone

from datetime import datetime

from .forms import NewListForm
from .models import MailingList
from .services import send_group


def mailing_list_page(request):
    """Вывод страницы со списком рассылок отсортированных по дате и кнопкой добавления новой рассылки"""
    tzname = None
    if 'tzname' in request.POST:
        print(request.POST['tzname'], '------------------')
        tzname = request.POST['tzname']
        request.session['tzname'] = tzname
    if not 'tzname' in request.session:
        tzname = 'not'
        request.session['tzname'] = 'not'

    mailing_list = MailingList.objects.all().order_by('date_of_completion')

    import datetime
    from django.utils import timezone
    time = timezone.localtime()
    time2 = timezone.localtime(timezone.now())
    naive = datetime.datetime.utcnow()
    # aware = timezone.now()
    # print(naive, aware, time, time2)

    now_datetime = timezone.now()
    print(now_datetime)
    # for i in mailing_list:
    #     print(i.date_of_completion.utcoffset(), now_datetime)

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
