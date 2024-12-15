from django.urls import path
from . import views

app_name = 'fortunaisk'

urlpatterns = [
    path('', views.index, name='index'),
    path('winners/', views.winners, name='winners'),
]
