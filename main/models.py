from django.db import models


class Currency(models.Model):
    """
    Модель валюты
    """
    name = models.CharField(max_length=150, unique=True, verbose_name='Название валюты')
    charcode = models.CharField(max_length=3, unique=True, verbose_name='Код валюты')

    def __str__(self):
        return f'{self.charcode}'

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'


class Rate(models.Model):
    """
    Модель курса валюты
    """
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name='Валюта')
    date = models.DateField(auto_now=True, verbose_name='Дата')
    rate = models.FloatField(verbose_name='Курс к рублю')

    def __str__(self):
        return f'{self.currency}: {self.date} - {self.rate}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('-date',)
