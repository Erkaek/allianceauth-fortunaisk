# admin.py
from django.contrib import admin
from .models import Ticket, Winner

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('character', 'ticket_ref', 'amount', 'paid', 'created_at')

@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
    list_display = ('character', 'ticket', 'won_at')