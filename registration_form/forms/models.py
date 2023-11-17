from django.db import models

# Create your models here.
class MyForms(models.Model):
    user_name = models.CharField(max_length=256, verbose_name='имя пользователя')
    email = models.EmailField(max_length=256, verbose_name='Email')
    phone = models.IntegerField(verbose_name='Телефон')
    data_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'форма регистрации'
        verbose_name_plural = 'Форма Регистрации'

    def __str__(self) -> str:
        return self.user_name