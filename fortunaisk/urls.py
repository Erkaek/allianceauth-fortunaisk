from django.urls import path
from . import views

app_name = 'fortunaisk'

urlpatterns = [
    path('', views.buy_tickets, name='buy_tickets'),  # Point de départ : /fortunaisk/
]
