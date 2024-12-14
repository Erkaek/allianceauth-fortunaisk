from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    purchased_at = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField()  # Number of tickets bought

    def __str__(self):
        return f"{self.user.username} - {self.amount} tickets"

class Pot(models.Model):
    total_amount = models.BigIntegerField(default=0)  # ISK total in the pot
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Pot created on {self.created_at} with {self.total_amount} ISK"

class Winner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wins')
    won_at = models.DateTimeField(auto_now_add=True)
    amount_won = models.BigIntegerField()

    def __str__(self):
        return f"{self.user.username} won {self.amount_won} ISK on {self.won_at}"
