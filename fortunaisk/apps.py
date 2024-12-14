from django.apps import AppConfig

class FortunaiskConfig(AppConfig):
    name = 'fortunaisk'
    verbose_name = "Fortuna ISK Raffle"

    def ready(self):
        import fortunaisk.signals  # Import des signaux si nécessaire
