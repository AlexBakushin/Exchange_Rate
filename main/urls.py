from main.apps import MainConfig
from django.urls import path
from rest_framework.routers import DefaultRouter
from main.views import CurrencyViewSet, RateListAPIView


app_name = MainConfig.name

router = DefaultRouter()
router.register(r'currency', CurrencyViewSet, basename='currency')

urlpatterns = [
    path('rate/', RateListAPIView.as_view(), name='rate_list'),
              ] + router.urls
