from django.contrib import admin
from .models import Lottery, LotteryEntry, LotteryWinner

@admin.register(Lottery)
class LotteryAdmin(admin.ModelAdmin):
    list_display = ('name', 'ticket_price', 'reference_code', 'start_date', 'end_date', 'is_active')

@admin.register(LotteryEntry)
class LotteryEntryAdmin(admin.ModelAdmin):
    list_display = ('lottery', 'user', 'character_name', 'wallet_transaction_id', 'date_purchased')
    search_fields = ('user__username', 'character_name')

@admin.register(LotteryWinner)
class LotteryWinnerAdmin(admin.ModelAdmin):
    list_display = ('lottery', 'user', 'date_drawn', 'prize_amount')
