from rest_framework import serializers
from main.models import Rate, Currency


class CurrencySerializer(serializers.ModelSerializer):
    rate = serializers.FloatField(source='rate_set.all.last.rate')
    date = serializers.DateField(source='rate_set.all.last.date')

    class Meta:
        model = Currency
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = '__all__'
