"""定义玩家的基本操作"""
from abc import ABC, abstractmethod
from enum import Enum

from cards.card import Card
from player.type import Identity


class BasePlayer(ABC):

    # 17 张普通手牌
    @property
    def normal_cards(self):
        return self._normal_cards

    @normal_cards.setter
    def normal_cards(self, cards: list[Card]):
        self._normal_cards = cards
        self._hold_cards = self.special_cards + self.normal_cards

    # 3 张底牌，谁是地主谁拿
    @property
    def special_cards(self):
        return self._special_cards

    @special_cards.setter
    def special_cards(self, cards: list[Card]):
        self._special_cards = cards
        self._hold_cards = self.special_cards + self.normal_cards

    @property
    def hold_cards(self):
        return self._hold_cards

    @hold_cards.setter
    def hold_cards(self, cards: list[Card]):
        self._hold_cards = cards

    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, identity: Identity):
        self._identity = identity

    def __init__(self, identity: Identity = None, normal_cards: list[Card] | None = None, special_cards: list[Card] | None = None):
        """
        用户拥有身份和牌

        :param identity: 玩家身份：农民 ｜ 地主
        :param normal_cards: 普通牌
        :param special_cards: 底牌
        """
        self._identity = identity or []
        self._normal_cards = normal_cards or []
        self._special_cards = special_cards or []
        self._hold_cards = self._normal_cards + self._special_cards

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

    @abstractmethod
    def call_the_landlord(self, max_point: int, cur_point: str) -> int:
        """
        玩家叫地主

        输出当前玩家叫分信息

        :param max_point: 当前最大的叫分
        :param cur_point: 当前玩家的叫分
        :return: 执行的操作码
            - 0: 玩家跳过此次叫分
            - 1: 当前玩家叫分最大，且不是 3
            - 2: 当前玩家叫分为 3
        """

    @abstractmethod
    def show_normol_cards(self):
        pass

    def card_sorting(self) -> list[Card]:
        """给玩家的持牌进行排序"""

        cards = self.hold_cards

        # 使用牌的等级进行排序，从小到大进行排序
        sorted_cards = sorted(cards, key = lambda card: card.value[2])
        self.hold_cards = sorted_cards

        return sorted_cards


