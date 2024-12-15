from django.urls import path
from . import views

app_name = 'fortunaisk'

urlpatterns = [
    path('tickets/', views.tickets_list, name='tickets_list'),
    path('winners/', views.winners_list, name='winners_list'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
]
