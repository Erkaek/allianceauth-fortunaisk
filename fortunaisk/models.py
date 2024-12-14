from django.db import models
from django.conf import settings
from django.utils import timezone
from allianceauth.eveonline.models import EveCharacter as Character


class RaffleTicket(models.Model):
    """
    Un ticket de loterie associé à un personnage spécifique.
    """
    character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        related_name='raffle_tickets'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='raffle_tickets'
    )
    purchase_date = models.DateTimeField(default=timezone.now)
    price_isk = models.BigIntegerField(default=0)  # Montant ISK payé pour le ticket
    payment_reference = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Ticket #{self.pk} - {self.user.username} - {self.character.character_name} - {self.price_isk} ISK"

    @property
    def is_valid(self):
        """
        Vérifie si le ticket est valide (par exemple, vérification de la date ou du paiement).
        """
        one_month_ago = timezone.now() - timezone.timedelta(days=30)
        return self.purchase_date >= one_month_ago


class RaffleWinner(models.Model):
    """
    Historique des gagnants mensuels.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    main_character = models.CharField(max_length=100, null=True, blank=True)
    total_pot = models.BigIntegerField(default=0)
    draw_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        date_str = self.draw_date.strftime('%Y-%m-%d %H:%M')
        return f"Gagnant du {date_str} - {self.user.username if self.user else 'Inconnu'}"

    @classmethod
    def last_winner(cls):
        """
        Retourne le dernier gagnant enregistré.
        """
        return cls.objects.order_by('-draw_date').first()
