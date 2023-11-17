from django import forms
from .models import *

class OrderForms(forms.Form):
    user_name = forms.CharField(max_length=255, label='Имя Пользователя')
    email = forms.EmailField(max_length=255, label='Email')
    phone = forms.IntegerField(label='Телефон')
    data_time = forms.DateTimeField(label='Дата')
    text = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}), label='Текст')

    class Meta():
        verbose_name = 'регистрации'
        verbose_name_plural = 'Форма Регистрации' 
