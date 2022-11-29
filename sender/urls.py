# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import mailing_list_page, new_list, open_mail

urlpatterns = [
    url('/new', new_list, name='new'),
    url('', mailing_list_page, name='list'),
]
