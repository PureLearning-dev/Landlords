from cards.card import Card
from player.base import BasePlayer
from player.type import Identity
from utils.doc_utils import inherit_docstring


@inherit_docstring
class UserPlayer(BasePlayer):

    def __init__(self, name: str = '游客', age: int = 18, identity: Identity = None, normal_cards: list[Card] | None = None, special_cards: list[Card] | None = None):
        super().__init__(identity, normal_cards, special_cards)
        self.name = name
        self.age = age

    def execute(self, previous_card, putcard) -> int:

        if UserPlayer.is_conform(previous_card, putcard):
            # 符合条件，可以打出
            # 所以需要将持有的牌中对应要打的牌移除
            self.hold_cards.remove(putcard)
            if len(self.hold_cards) == 0:
                return 3
            return 1

        return 2

    def call_the_landlord(self, max_point: int, cur_point: str) -> int:
        # 规格化玩家输入内容
        fix_cur_point = cur_point.strip().lower()

        # 若玩家输入的不在 ['1', '2', '3'] 中或者小于最大叫分值，则视为跳过
        if fix_cur_point not in ['1', '2', '3'] or int(fix_cur_point) <= max_point:
            print(f"{self.name} 跳过此次叫地主")
            return 0
        # 如果当前玩家输入的分数合理
        elif int(fix_cur_point) > max_point:
            # 如果当前玩家叫分为 3，则停止，且修改最大叫分玩家
            if int(fix_cur_point) == 3:
               print(f"{self.name} 叫分为：3，直接成为地主，不再进行后续叫号")
               return 2
            # 否则需要修改地主，并可以继续执行
            print(f"{self.name} 叫分为：{cur_point}")
            return 1

        return 3

    def show_normol_cards(self):
        return self.hold_cards

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.age}, {self.identity}, {self.normal_cards}, {self.special_cards})"