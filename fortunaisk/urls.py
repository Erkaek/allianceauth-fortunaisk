from django.urls import path
from .views import main_view, history_view

app_name = 'fortunaisk'

urlpatterns = [
    path('', main_view, name='main'),
    path('history/', history_view, name='history'),
]
