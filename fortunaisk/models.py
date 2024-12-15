from django.db import models
from django.conf import settings
from django.utils import timezone

class Lottery(models.Model):
    name = models.CharField(max_length=255)
    ticket_price = models.DecimalField(max_digits=15, decimal_places=2, help_text="Prix du ticket en ISK")
    reference_code = models.CharField(max_length=50, unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class LotteryEntry(models.Model):
    lottery = models.ForeignKey(Lottery, on_delete=models.CASCADE, related_name='entries')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    character_name = models.CharField(max_length=100)
    wallet_transaction_id = models.BigIntegerField(null=True, blank=True)
    date_purchased = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user} - {self.lottery.name}"

class LotteryWinner(models.Model):
    lottery = models.OneToOneField(Lottery, on_delete=models.CASCADE, related_name='winner')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    date_drawn = models.DateTimeField(default=timezone.now)
    prize_amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Gagnant de {self.lottery.name}"
