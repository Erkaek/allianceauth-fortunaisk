# fortunaisk/urls.py

from django.urls import path
from . import views

app_name = 'fortunaisk'  # Nécessaire pour le namespace

urlpatterns = [
    path('', views.current_lottery, name='current_lottery'),
    path('winners/', views.winners_history, name='winners_history'),
]
