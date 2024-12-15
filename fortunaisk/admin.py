from django.contrib import admin
from .models import LotteryConfig, LotteryWinner

@admin.register(LotteryConfig)
class LotteryConfigAdmin(admin.ModelAdmin):
    list_display = ('reference_id', 'ticket_price', 'corporation_id')

@admin.register(LotteryWinner)
class LotteryWinnerAdmin(admin.ModelAdmin):
    list_display = ('username', 'prize', 'date')
