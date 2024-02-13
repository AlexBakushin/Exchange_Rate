from rest_framework import viewsets, generics
from main.serliazers import CurrencySerializer, RateSerializer
from main.models import Rate, Currency
from django_filters.rest_framework import DjangoFilterBackend, CharFilter, FilterSet


class CurrencyViewSet(viewsets.ModelViewSet):
    """
    класс представления валют через viewset
    """
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()


class RateFilter(FilterSet):
    """
    включение фильтрации у курса по коду валюты
    """
    charcode = CharFilter(field_name='currency__charcode')

    class Meta:
        model = Rate
        fields = ['charcode', 'date']


class RateListAPIView(generics.ListAPIView):
    """
    класс представления от дженериков для получения списка курсов валют с доп. фильтрацией
    """
    serializer_class = RateSerializer
    queryset = Rate.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = RateFilter
