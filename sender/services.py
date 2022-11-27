# -*- coding: utf-8 -*-
from datetime import timedelta
from django.utils import timezone

from subscriber.models import Subscriber
from .models import MailingList
from mailganer.tasks import send_mail

def send_group(new_list):
    """Отправка писем группе"""
    # new_list = MailingList.objects.filter(id='286dc9d7-afc8-4029-ace1-5cc5e649c311')[0]
    subscribers = Subscriber.objects.filter(group=new_list.group).only('id')  # Запрос id получателей
    delta = (new_list.date_of_completion.replace(tzinfo=None) - timezone.now().replace(tzinfo=None)).total_seconds() // 60
    print(delta)
    for subscriber in subscribers:
        # if timezone.now() >= new_list.date_of_completion:
        send_mail.apply_async([subscriber.id, new_list.sample.sample], eta=new_list.date_of_completion)


def set_tzname(request):
    """Получение имени временной зоны из JS со страницы и запись его в сессию для middleware
    передача в шаблон,для проверки на стороне клиента актуальности впеменной зоны"""
    # del request.session['tzname']
    tzname = 'not'
    if 'tzname' in request.POST:
        print(request.POST['tzname'])
        tzname = request.POST['tzname']
        request.session['tzname'] = tzname
    else:
        if 'tzname' in request.session:
            tzname = request.session['tzname']
    return tzname
