# fortunaisk/models.py

from django.db import models
from django.contrib.auth.models import User

class Lottery(models.Model):
    name = models.CharField(max_length=255)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    reference_code = models.CharField(max_length=100, unique=True)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    entries = models.ManyToManyField(User, related_name='lottery_entries', blank=True)
    winner = models.ForeignKey(User, related_name='lottery_wins', on_delete=models.SET_NULL, null=True, blank=True)
    prize_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    date_drawn = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
