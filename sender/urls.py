# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import mailing_list_page, new_list, report


urlpatterns = [
    url('new', new_list, name='new'),
    url('report/(?P<list_id>.+)', report, name='report'),
    url('', mailing_list_page, name='list'),
]
