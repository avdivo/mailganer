"""mailganer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('list', include('sender.urls')),

]

import time
from .tasks import send_report
from django.utils import timezone
from datetime import timedelta
from mailganer.celery import celery_app

# send_report.apply_async([5], eta=timezone.now() + timedelta(minutes=5))
# send_report.apply_async([4], eta=timezone.now() + timedelta(minutes=4))
# send_report.apply_async([3], eta=timezone.now() + timedelta(minutes=3))
g = send_report.apply_async([1], eta=timezone.now() + timedelta(seconds=5))
print('==============================', g.id)
celery_app.control.revoke(g.id, terminate=True)
send_report.apply_async([g.id], eta=timezone.now() + timedelta(seconds=5))
send_report.apply_async([3], eta=timezone.now() + timedelta(seconds=5))

send_report.apply_async([4], eta=timezone.now() + timedelta(seconds=5))
send_report.apply_async([5], eta=timezone.now() + timedelta(seconds=5))
send_report.apply_async([6], eta=timezone.now() + timedelta(seconds=5))

send_report.apply_async([201], eta=timezone.now() + timedelta(seconds=5))
send_report.apply_async([202], eta=timezone.now() + timedelta(seconds=5))
send_report.apply_async([203], eta=timezone.now() + timedelta(seconds=5))

send_report.apply_async([204], eta=timezone.now() + timedelta(seconds=5))
send_report.apply_async([205], eta=timezone.now() + timedelta(seconds=5))
send_report.apply_async([206], eta=timezone.now() + timedelta(seconds=5))

send_report.apply_async([207], eta=timezone.now() + timedelta(seconds=5))
send_report.apply_async([208], eta=timezone.now() + timedelta(seconds=5))
send_report.apply_async([209], eta=timezone.now() + timedelta(seconds=5))