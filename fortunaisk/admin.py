from django.contrib import admin
from .models import Ticket, Pot, Winner

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'purchased_at')

@admin.register(Pot)
class PotAdmin(admin.ModelAdmin):
    list_display = ('total_amount', 'created_at')

@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount_won', 'won_at')
