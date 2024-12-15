from django.urls import path
from . import views

app_name = "fortunaisk"

urlpatterns = [
    path("tickets/", views.ticket_list, name="ticket_list"),  # URL pour afficher les tickets
    path("winners/", views.winner_list, name="winner_list"),  # URL pour afficher les gagnants
]
