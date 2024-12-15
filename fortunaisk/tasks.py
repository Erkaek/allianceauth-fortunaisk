from celery import shared_task
from django.utils import timezone
from .models import Lottery, LotteryEntry
from .helpers import filter_transactions_for_lottery
from django.conf import settings
from allianceauth.eveonline.models import EveCharacter
from allianceauth.services.tasks import QueueOnce

# Importez la fonction similaire à celle utilisée par invoice_manager pour récupérer les transactions
from invoice_manager.utils import fetch_corporation_wallet_journal

@shared_task(base=QueueOnce, lock_expire=60)
def verify_ticket_payments():
    # On prend les loteries actives
    active_lotteries = Lottery.objects.filter(is_active=True, end_date__gte=timezone.now())
    if not active_lotteries:
        return

    # Pour chaque loterie, on récupère les transactions du wallet corp
    # Le Invoice Manager prévoit généralement une configuration du personnage corporatif.
    # On suppose que vous avez un personnage corp configuré pour les transactions
    corp_char = EveCharacter.objects.filter(is_corporation=True).first()
    if not corp_char:
        return

    # On récupère les transactions (journal) du wallet corporation
    # fetch_corporation_wallet_journal(corp_char) est une fonction du invoice_manager (adaptée ici)
    # qui retourne une liste de dictionnaires avec 'transaction_id', 'amount', 'description', 'date', 'character_name' etc.
    transactions = fetch_corporation_wallet_journal(corp_char)

    for lottery in active_lotteries:
        filtered_tx = filter_transactions_for_lottery(transactions, lottery)
        for tx in filtered_tx:
            # On doit lier le ticket à un utilisateur. Le principe est similaire à l’Invoice Manager :
            # On cherche un utilisateur possédant un personnage avec le nom tx['character_name'].
            # On suppose que tx['character_name'] est présent dans l'ESI data.
            # Sinon, on pourra stocker le ticket sans user, ou tenter de trouver user par character.
            
            # On récupère le personnage par nom :
            char = EveCharacter.objects.filter(character_name=tx['character_name']).first()
            if not char or not char.owner:
                # Si on ne trouve pas l’utilisateur, on ignore ou on crée un ticket "anonyme"
                # mais de préférence on a un character relié à un user (grâce à AllianceAuth)
                continue
            
            user = char.owner.user

            LotteryEntry.objects.create(
                lottery=lottery,
                user=user,
                character_name=tx['character_name'],
                wallet_transaction_id=tx['transaction_id'],
                date_purchased=tx['date']
            )
