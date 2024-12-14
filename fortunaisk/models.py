from django.db import models
from django.conf import settings
from django.utils import timezone

class RaffleTicket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='raffle_tickets'
    )
    price_isk = models.BigIntegerField(default=0)
    payment_reference = models.CharField(max_length=100, unique=True)
    purchase_date = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ("view_raffle", "Can view the raffle module"),
        ]

    def __str__(self):
        return f"Ticket #{self.id} - {self.user.username} - {self.price_isk} ISK"


class RaffleWinner(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    total_pot = models.BigIntegerField(default=0)
    draw_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Gagnant du {self.draw_date.strftime('%Y-%m-%d')} - {self.user.username if self.user else 'Inconnu'}"
