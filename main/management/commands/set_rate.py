from django.core.management import BaseCommand
import requests
import json
from main.models import Rate, Currency


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        json_list = json.loads(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').content.decode())
        for currency_code, currency_data in json_list.get('Valute').items():
            currency = Currency.objects.filter(charcode=currency_data['CharCode']).first()
            if currency:
                rate = Rate.objects.create(
                    currency=currency,
                    date=json_list['Date'],
                    rate=currency_data['Value']
                )
                rate.save()
                print(rate)
        print('Значения курсов валют успешно записанны в базу данных')

