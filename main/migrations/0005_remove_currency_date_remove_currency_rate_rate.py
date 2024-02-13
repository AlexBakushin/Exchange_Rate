# Generated by Django 4.2.7 on 2024-02-13 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_currency_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency',
            name='date',
        ),
        migrations.RemoveField(
            model_name='currency',
            name='rate',
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='Дата')),
                ('rate', models.FloatField(verbose_name='Курс к рублю')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.currency', verbose_name='Валюта')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
