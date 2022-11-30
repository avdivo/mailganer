# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import EmailMessage


# Отправление Email -------------------------------------------------------------------
#   message - отрендереный html документ, to - кому письмо
def send_email(message, to):
    """Отправить письмо в HTML формате"""
    subject = 'GreenSoap'
    from_email = settings.EMAIL_HOST_USER
    msg = EmailMessage(subject, message, from_email=from_email, to=to)
    msg.content_subtype = 'html'
    try:
        msg.send()
    except:
        return False
    return True
