from django.contrib import admin
from .models import RaffleTicket, RaffleWinner

@admin.register(RaffleTicket)
class RaffleTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'character', 'price_isk', 'purchase_date', 'payment_reference')
    list_filter = ('purchase_date', 'price_isk')
    search_fields = ('user__username', 'character__name', 'payment_reference')

@admin.register(RaffleWinner)
class RaffleWinnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'main_character', 'total_pot', 'draw_date')
    list_filter = ('draw_date', 'total_pot')
    search_fields = ('user__username', 'main_character')
