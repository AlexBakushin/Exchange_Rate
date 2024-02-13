from django.contrib import admin
from main.models import Currency, Rate


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    """
    Зарегистрировал в админке модель валюты
    """
    list_display = ('name', 'charcode',)
    list_filter = ('name', 'charcode',)
    search_fields = ('name', 'charcode',)


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    """
    Зарегистрировал в админке модель курса валюты
    """
    list_display = ('currency', 'date', 'rate',)
    list_filter = ('date', 'currency',)
    search_fields = ('date', 'currency',)


