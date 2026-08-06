"""定义玩家的基本操作"""

from abc import ABC, abstractmethod
from locale import normalize

from cards.card import Card
from player.type import Identity


class BasePlayer(ABC):

    # 17 张普通手牌
    @property
    def normal_cards(self):
        return self.normal_cards

    @normal_cards.setter
    def normal_card(self, cards: list[Card]):
        self.normal_cards = cards
        self.hold_cards = self.special_cards + self.normal_cards

    # 3 张底牌，谁是地主谁拿
    @property
    def special_cards(self):
        return self.special_cards

    @special_cards.setter
    def special_cards(self, cards: list[Card]):
        self.special_cards = cards
        self.hold_cards = self.special_cards + self.normal_cards

    # 最终持有的手牌
    hold_cards: list[Card] = []

    def __init__(self, identity: Identity = None, normal_cards: list[Card] = [], special_cards: list[Card] = []):
        """
        用户拥有身份和牌

        :param identity: 玩家身份：农民 ｜ 地主
        :param normal_cards: 普通牌
        :param special_cards: 底牌
        """
        self.identity = identity
        self.normal_cards = normal_cards
        self.special_cards = special_cards
        self.hold_cards = normal_cards + special_cards

    @abstractmethod
    def execute(self, previous_card: Card, cur_card: Card):
        """"
        玩家出牌

        :param previous_card: 前一张牌
        :param cur_card: 当前打出的牌
        :return: int
            1 表示正确打出，并且符合规则
            2 表示不符合规则
            3 表示牌出完了，游戏结束
        """
        pass

    @staticmethod
    def call_the_landlord(max_point: int, cur_point: str):
        """
        玩家叫地主

        :param max_point: 当前最大的叫分
        :param cur_point: 当前玩家的叫分
        :return: 是否继续叫地主 int
            - 0：停止叫地主，且不修改最大叫分用户
            - 1: 停止叫地主，且修改最大叫分用户
            - 2：继续叫地主，且不修改最大叫分用户
            - 3: 继续叫地主，且修改最大叫分用户
        """

        fix_cur_point = cur_point.strip().lower()

        # 如果最大叫分为 3 了，则直接停止，且不修改最大叫分的用户
        if max_point == 3:
            return 0
        # 如果当前用户叫分为 3，则停止，且修改最大叫分用户
        if int(fix_cur_point) == 3:
            return 1
        # 如果用户跳过，则继续叫地主，且不修改最大叫分用户
        if fix_cur_point not in [1, 2, 3]:
            return 2
        if int(fix_cur_point) > max_point:
            return 3