# -*- coding: utf-8 -*-
from django import forms

from .models import MailingList


class NewListForm(forms.ModelForm):
    """Форма для создания новой рассылки"""
    # Исправляем формат принимаемой даты от кастомного виджета
    date_of_completion = forms.DateTimeField(widget=forms.DateTimeInput(format='%Y-%m-%dT%H:%M'), input_formats=('%Y-%m-%dT%H:%M',), required=False)
    class Meta:
        model = MailingList
        fields = ('name', 'date_of_completion', 'group', 'sample')

