from django.core.management import BaseCommand
import requests
import json
from main.models import Currency


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        json_list = json.loads(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').content.decode())
        for currency_code, currency_data in json_list.get('Valute').items():
            currency = Currency.objects.create(
                name=currency_data['Name'],
                charcode=currency_data['CharCode'],
            )
            currency.save()
            print(currency)

