from django.contrib import admin
from .models import RaffleTicket, RaffleWinner

@admin.register(RaffleTicket)
class RaffleTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'character', 'price_isk', 'purchase_date')

@admin.register(RaffleWinner)
class RaffleWinnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'main_character', 'total_pot', 'draw_date')
