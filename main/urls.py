from main.apps import MainConfig
from django.urls import path

app_name = MainConfig.name

urlpatterns = [
                 # path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
              ]
