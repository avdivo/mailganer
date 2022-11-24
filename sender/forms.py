# -*- coding: utf-8 -*-
from django import forms

from .models import MailingList


class NewListForm(forms.ModelForm):
    """Форма для создания новой рассылки"""
    class Meta:
        model = MailingList
        fields = ('name', 'date_of_completion', 'group', 'sample')
