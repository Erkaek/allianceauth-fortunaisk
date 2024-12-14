# fortunaisk/urls.py
from django.urls import path
from .views import index

app_name = 'fortunaisk'

urlpatterns = [
    path('', index, name='index'),
]
