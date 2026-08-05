"""定义玩家的基本操作"""

from abc import ABC, abstractmethod
from locale import normalize

from cards.type import Card
from player.type import Identity


class BasePlayer(ABC):

    # 17 张普通手牌
    normal_cards: list[Card] = []

    # 3 张底牌，谁是地主谁拿
    special_cards: list[Card] = []

    # 最终持有的手牌
    hold_cards: list[Card] = []

    def __init__(self, identity: Identity, normal_cards: list[Card], special_cards: list[Card]):
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

    @abstractmethod
    def call_the_landlord(self, max_point: int, cur_point: str):
        """
        叫地主

        必须比当前最高得分高，并且只能叫一次

        :param max_point: 当前叫的最大值
        :param cur_point: 现在叫的值
        :return: int
            1 表示成功叫得分数
            0 表示跳过
        """
        pass