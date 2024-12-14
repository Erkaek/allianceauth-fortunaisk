# fortunaisk/models.py
from django.db import models
from django.conf import settings

class FortuneRecord(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='fortune_records'
    )
    amount = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.amount} ISK"
