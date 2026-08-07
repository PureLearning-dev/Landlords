from cards.card import Card
from game.card_type import type_judgment
from player.base import BasePlayer
from player.user import UserPlayer


class TestCardType:

    def __init__(self, cards: list[Card] = None, user: BasePlayer = None):
        if cards is None:
            cards = [Card.CLUB_5, Card.BIG_JOKER, Card.CLUB_6, Card.CLUB_4, Card.CLUB_7, Card.DIAMOND_7, Card.DIAMOND_4, Card.SPADE_A, Card.SPADE_Q]
        if user is None:
            user = UserPlayer()
            user.normal_cards = cards

        self.cards = cards
        self.user = user

    def test_demo(self):
        demo = {
            1: 'hell0',
            'int': 'world'
        }
        print(demo.keys())
        print(demo.values())
        print(list(demo.values()))
        print(set(demo.values()))

    def test_card_type_judgment(self):

        # 在后续实现玩家打牌后，需要将打出的牌进行排序
        test_data: list[list[Card]] = [
            # ── 跳过 ──
            [],

            # ── 单张 ──
            [Card.BIG_JOKER],

            # ── 对子 ──
            [Card.CLUB_2, Card.DIAMOND_2],

            # ── 三张 ──
            [Card.CLUB_4, Card.DIAMOND_4, Card.SPADE_4],

            # ── 三带一 ──
            [Card.CLUB_5, Card.DIAMOND_5, Card.SPADE_5, Card.CLUB_9],

            # ── 三带二 ──
            [Card.CLUB_5, Card.DIAMOND_5, Card.SPADE_5, Card.CLUB_9, Card.DIAMOND_9],

            # ── 顺子（5 张起，2 和王不能进）──
            [Card.SPADE_3, Card.HEART_4, Card.CLUB_5, Card.DIAMOND_6, Card.SPADE_7],

            # ── 连对（3 连对起）──
            [Card.SPADE_3, Card.HEART_3, Card.CLUB_4, Card.DIAMOND_4, Card.SPADE_5, Card.HEART_5],

            # ── 飞机（2 连三张起）──
            [Card.SPADE_3, Card.HEART_3, Card.CLUB_3,
             Card.DIAMOND_4, Card.SPADE_4, Card.HEART_4],

            # ── 飞机带单张 ──
            [Card.SPADE_3, Card.HEART_3, Card.CLUB_3,
             Card.DIAMOND_4, Card.SPADE_4, Card.HEART_4,
             Card.CLUB_8, Card.DIAMOND_10],

            # ── 飞机带对子 ──
            [Card.SPADE_3, Card.HEART_3, Card.CLUB_3,
             Card.DIAMOND_4, Card.SPADE_4, Card.HEART_4,
             Card.CLUB_8, Card.DIAMOND_8,
             Card.SPADE_10, Card.HEART_10],

            # ── 四带两单 ──
            [Card.SPADE_7, Card.HEART_7, Card.CLUB_7, Card.DIAMOND_7,
             Card.CLUB_3, Card.SPADE_9],

            # ── 四带两对 ──
            [Card.SPADE_7, Card.HEART_7, Card.CLUB_7, Card.DIAMOND_7,
             Card.CLUB_3, Card.DIAMOND_3,
             Card.SPADE_9, Card.HEART_9],

            # ── 炸弹 ──
            [Card.SPADE_Q, Card.HEART_Q, Card.CLUB_Q, Card.DIAMOND_Q],

            # ── 火箭 ──
            [Card.SMALL_JOKER, Card.BIG_JOKER],
        ]

        for cards in test_data:
            cards_type = type_judgment(cards)
            print(cards_type)

    def test_sort_card(self):
        print(f"{'-' * 50} 未排序的牌 {'-' * 50}")
        print(self.cards)

        print(f"{'-' * 50} 排序后的牌 {'-' * 50}")
        self.user.card_sorting()
        print(self.user.hold_cards)



if __name__ == '__main__':
    test = TestCardType()
    # test.test_demo()
    # test.test_card_type_judgment()
    test.test_sort_card()