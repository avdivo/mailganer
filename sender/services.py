# -*- coding: utf-8 -*-
from subscriber.models import Subscriber
from mailganer.tasks import send_mail


def send_group(new_list, site_url):
    """Отправка писем группе"""
    subscribers = Subscriber.objects.filter(group=new_list.group).only('id')  # Запрос id получателей
    for subscriber in subscribers:
        # Передем в Task ссылки на записи БД с данными о получателе и рассылке
        send_mail.apply_async([subscriber.id, new_list.id, site_url], eta=new_list.date_of_completion)


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
