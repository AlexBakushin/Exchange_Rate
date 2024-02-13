import logging
from datetime import datetime, timedelta
from django.conf import settings
from django.utils import timezone
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from main.models import Currency, Rate
import json
import requests


logger = logging.getLogger(__name__)


def my_job():
    print('Задача запущена')
    timezone.activate('Asia/Yekaterinburg')
    today = datetime.now().strftime("%Y-%m-%d")
    if Rate.objects.all():
        rate_date = Rate.objects.all().last().date.strftime("%Y-%m-%d")

    else:
        rate_date = '2024-02-12'

    if rate_date != today:
        print('Начало проверки последней даты')
        try:
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
            print('Значения курсов валют успешно записанны в базу данных!')
            print(f'Следующая проверка будет произведена {(datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")} в это же время!')

        except requests.exceptions.Timeout:
            print('Вероятно сервер болеет, попробуйте обратиться к нему позже')

        except requests.exceptions.TooManyRedirects:
            print('Вероятно некорректный URL')

        except requests.ConnectionError:
            print('Нет соединения с сервером')


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")
        scheduler.add_job(
            my_job,
            trigger=CronTrigger(day="*/1"),
            id="my_job",
            max_instances=1,
            replace_existing=True,
        )
        try:
            scheduler.start()
        except KeyboardInterrupt:
            scheduler.shutdown()
