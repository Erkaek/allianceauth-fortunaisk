# fortunaisk/urls.py
from django.urls import path, include
from .views import index

app_name = 'fortunaisk'

urlpatterns = [
    path('', index, name='index'),
    path('fortunaisk/', include('fortunaisk.urls', namespace='fortunaisk')),
]
