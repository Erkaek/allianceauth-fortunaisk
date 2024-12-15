from allianceauth.services.tasks import QueueOnce
from datetime import timedelta
from django.utils import timezone
from .models import LotteryEntry

def filter_transactions_for_lottery(transactions, lottery):
    """
    Filtre les transactions corporate pour celles correspondant à la loterie donnée.
    Critères :
    - Le champ 'description' doit contenir le code de référence de la loterie
    - Le montant doit être égal au ticket_price
    """
    filtered = []
    for tx in transactions:
        if lottery.reference_code in tx['description'] and tx['amount'] == float(lottery.ticket_price):
            # On vérifie qu'on n'a pas déjà enregistré cette transaction
            if not LotteryEntry.objects.filter(wallet_transaction_id=tx['transaction_id']).exists():
                filtered.append(tx)
    return filtered
