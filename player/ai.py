from cards.card import Card
from player.base import BasePlayer


class AIPlayer(BasePlayer):

    def execute(self, previous_card: Card, cur_card: Card):
        pass

    def call_the_landlord(self, max_point: int, cur_point: str) -> int:
        pass

    def show_normol_cards(self):
        pass