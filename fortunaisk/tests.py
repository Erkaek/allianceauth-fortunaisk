from django.test import TestCase
from django.contrib.auth.models import User
from .models import Ticket, Pot, Winner
from .tasks import draw_winner

class FortunaISKTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.pot = Pot.objects.create(total_amount=0)

    def test_buy_ticket(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post("/buy-tickets/", {"amount": 5})
        self.assertEqual(Ticket.objects.count(), 1)
        self.assertEqual(Pot.objects.last().total_amount, 5000000)

    def test_draw_winner(self):
        Ticket.objects.create(user=self.user, amount=10)
        self.pot.total_amount = 10000000
        self.pot.save()

        draw_winner()

        winner = Winner.objects.last()
        self.assertIsNotNone(winner)
        self.assertEqual(winner.amount_won, 10000000)
