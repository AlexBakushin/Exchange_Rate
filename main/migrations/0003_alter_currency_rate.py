# Generated by Django 4.2.7 on 2024-02-13 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_currency_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='rate',
            field=models.PositiveSmallIntegerField(verbose_name='Курс к рублю'),
        ),
    ]
