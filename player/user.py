from cards.type import Card
from player.base import BasePlayer
from utils.doc_utils import inherit_docstring


@inherit_docstring
class UserPlayer(BasePlayer):

    @staticmethod
    def is_conform(pre: Card, cur: Card) -> bool:
        return True

    def execute(self, previous_card, putcard) -> int:

        if UserPlayer.is_conform(previous_card, putcard):
            # 符合条件，可以打出
            # 所以需要将持有的牌中对应要打的牌移除
            self.hold_cards.remove(putcard)
            if len(self.hold_cards) == 0:
                return 3
            return 1

        return 2

    def call_the_landlord(self, max_point, cur_point) -> int:
        fix_cur_point = cur_point.strip().lower()

        if max_point == 3 or fix_cur_point not in ['1', '2', '3'] or int(fix_cur_point) <= max_point:
            return 0

        return 1
