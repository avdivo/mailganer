import pytz

from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

class TimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # tzname = request.session.get('django_timezone')
        # if tzname:
        tzname = 'Europe/Moscow'
        # tzname = 'America/Anchorage'
        # print('-------------------------------------------------------------------')
        timezone.activate(pytz.timezone(tzname))
        # else:
        #     timezone.deactivate()
        pass