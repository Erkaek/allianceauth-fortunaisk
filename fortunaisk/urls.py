from django.urls import path
from . import views

app_name = 'fortunaisk'

urlpatterns = [
    path('buy-tickets/', views.buy_tickets, name='buy_tickets'),
]
