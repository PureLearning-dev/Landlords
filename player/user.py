from cards.card import Card
from player.base import BasePlayer
from utils.doc_utils import inherit_docstring


@inherit_docstring
class UserPlayer(BasePlayer):

    def execute(self, previous_card, putcard) -> int:

        if UserPlayer.is_conform(previous_card, putcard):
            # 符合条件，可以打出
            # 所以需要将持有的牌中对应要打的牌移除
            self.hold_cards.remove(putcard)
            if len(self.hold_cards) == 0:
                return 3
            return 1

        return 2