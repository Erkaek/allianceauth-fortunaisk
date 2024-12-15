from django.db import models

class LotteryConfig(models.Model):
    ticket_price = models.DecimalField(max_digits=20, decimal_places=2, default=10000000)  # 10M ISK par défaut
    reference_id = models.CharField(max_length=255, unique=True)  # Référence unique
    corporation_id = models.BigIntegerField()  # ID de la corporation

    def __str__(self):
        return f"Loterie {self.reference_id}"

class LotteryWinner(models.Model):
    username = models.CharField(max_length=255)
    prize = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} won {self.prize} ISK on {self.date}"
