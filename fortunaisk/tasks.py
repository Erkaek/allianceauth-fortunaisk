from corp_tools.models import WalletJournalEntry
from .models import LotteryConfig, LotteryWinner

def check_payments():
    config = LotteryConfig.objects.last()
    if not config:
        print("Aucune configuration de loterie trouvée.")
        return

    entries = WalletJournalEntry.objects.filter(
        owner_id=config.corporation_id,
        amount=-config.ticket_price,
        reason__icontains=config.reference_id
    )

    for entry in entries:
        # Logique pour ajouter des participants ou identifier le gagnant
        print(f"Payment received from {entry.sender_name} for lottery.")
