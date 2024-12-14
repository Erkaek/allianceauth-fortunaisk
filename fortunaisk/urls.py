from django.urls import path
from . import views

app_name = 'fortunaisk'

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('history/', views.history_view, name='history_view'),
]
