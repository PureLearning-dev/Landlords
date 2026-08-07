"""定义出牌的类型"""
from enum import StrEnum
from cards.card import Card

class CardType(StrEnum):
    """斗地主牌型"""

    SINGLE = "单张"
    PAIR = "对子"
    THREE = "三张"
    THREE_WITH_ONE = "三带一"
    THREE_WITH_PAIR = "三带二"
    STRAIGHT = "顺子"
    PAIR_STRAIGHT = "连对"
    AIRPLANE = "飞机"
    AIRPLANE_WITH_SINGLES = "飞机带单张"
    AIRPLANE_WITH_PAIRS = "飞机带对子"
    FOUR_WITH_TWO = "四带两单"
    FOUR_WITH_TWO_PAIRS = "四带两对"
    BOMB = "炸弹"
    ROCKET = "火箭"
    SKIP = '跳过'

def _group_by_rank(cards: list[Card]) -> dict[int, int]:
    """
    将玩家打的牌按照等级分组

    :param cards: 玩家打的牌
    :return: 玩家打出的牌的分组信息
    """

    # 定义维护牌信息分组
    cards_info = {}

    for card in cards:
        # 当牌的分数在 card_info 中，则将该分数的计数加一，否则令其计数为一
        cards_info[card.game_value] = cards_info.get(card.game_value, 0) + 1

    return cards_info

def type_judgment(cards: list[Card] | None = None) -> CardType:
    """
    判断玩家打牌的类型

    先将玩家打得牌按照等级分好类，然后根据分类进行进一步判断

    :param cards: 玩家打出的牌
    :return: 玩家打出的牌的类型
    """
    if cards is None:
        # 要重新声明变量的类型，才会让编译器知道这个变量的类型发生改变了，不然还是函数参数中的 list[Card] | None
        cards: list[Card] = []

    # 得到玩家打牌的分组信息
    cards_info = _group_by_rank(cards)

    print(f"{'-' * 50} 得到玩家打出牌的分组信息 {'-' * 50}")
    print(cards_info)

    # 得到打出牌的 值 和其对应的 张数
    card_game_values = list(cards_info.keys())
    card_game_values_num = list(cards_info.values())

    print(f"{'-' * 50} 规格化出牌的分组信息 {'-' * 50}")
    print(f"card_game_values: {card_game_values}")
    print(f"card_game_values_num: {card_game_values_num}")

    # 判断牌的类型

    # 玩家如果输入的不是牌，则视为空，在这里就可以跳过了
    # 1. 判断是否为跳过 [没有一张牌]
    if not cards_info:
        return CardType.SKIP
    # 2. 判断是否为单张
    elif card_game_values_num == [1]:
        return CardType.SINGLE
    # 3. 判断是否为对子 [牌的分组数为 1，且有两张等级相同的牌]
    elif card_game_values_num == [2]:
        return CardType.PAIR
    # 4. 判断是否为火箭
    elif card_game_values == [16, 17]:
        return CardType.ROCKET
    # 5. 判断是否为三张
    elif card_game_values_num == [3]:
        return CardType.THREE
    # 6. 判断是否为三带一
    elif len(card_game_values) == 2 and 3 in card_game_values_num:
        pass

    return CardType.SKIP

def _is_continuous(cards: list[int]) -> bool:
    """
    判断牌是否是连续的

    :param cards: 牌的等级
    :return: 是否为连续的一组牌
    """
    pass
