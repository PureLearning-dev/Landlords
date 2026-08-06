"""定义牌相关的信息"""

from __future__ import annotations
from enum import Enum
from typing import Optional


class Card(Enum):
    """斗地主牌值：3 最小(3)，依次递增，A(14), 2(15), 小王(16), 大王(17)"""

    # ── 黑桃 ──
    SPADE_3 = ("♠", "3", 3)
    SPADE_4 = ("♠", "4", 4)
    SPADE_5 = ("♠", "5", 5)
    SPADE_6 = ("♠", "6", 6)
    SPADE_7 = ("♠", "7", 7)
    SPADE_8 = ("♠", "8", 8)
    SPADE_9 = ("♠", "9", 9)
    SPADE_10 = ("♠", "10", 10)
    SPADE_J = ("♠", "J", 11)
    SPADE_Q = ("♠", "Q", 12)
    SPADE_K = ("♠", "K", 13)
    SPADE_A = ("♠", "A", 14)
    SPADE_2 = ("♠", "2", 15)

    # ── 红桃 ──
    HEART_3 = ("♥", "3", 3)
    HEART_4 = ("♥", "4", 4)
    HEART_5 = ("♥", "5", 5)
    HEART_6 = ("♥", "6", 6)
    HEART_7 = ("♥", "7", 7)
    HEART_8 = ("♥", "8", 8)
    HEART_9 = ("♥", "9", 9)
    HEART_10 = ("♥", "10", 10)
    HEART_J = ("♥", "J", 11)
    HEART_Q = ("♥", "Q", 12)
    HEART_K = ("♥", "K", 13)
    HEART_A = ("♥", "A", 14)
    HEART_2 = ("♥", "2", 15)

    # ── 梅花 ──
    CLUB_3 = ("♣", "3", 3)
    CLUB_4 = ("♣", "4", 4)
    CLUB_5 = ("♣", "5", 5)
    CLUB_6 = ("♣", "6", 6)
    CLUB_7 = ("♣", "7", 7)
    CLUB_8 = ("♣", "8", 8)
    CLUB_9 = ("♣", "9", 9)
    CLUB_10 = ("♣", "10", 10)
    CLUB_J = ("♣", "J", 11)
    CLUB_Q = ("♣", "Q", 12)
    CLUB_K = ("♣", "K", 13)
    CLUB_A = ("♣", "A", 14)
    CLUB_2 = ("♣", "2", 15)

    # ── 方块 ──
    DIAMOND_3 = ("♦", "3", 3)
    DIAMOND_4 = ("♦", "4", 4)
    DIAMOND_5 = ("♦", "5", 5)
    DIAMOND_6 = ("♦", "6", 6)
    DIAMOND_7 = ("♦", "7", 7)
    DIAMOND_8 = ("♦", "8", 8)
    DIAMOND_9 = ("♦", "9", 9)
    DIAMOND_10 = ("♦", "10", 10)
    DIAMOND_J = ("♦", "J", 11)
    DIAMOND_Q = ("♦", "Q", 12)
    DIAMOND_K = ("♦", "K", 13)
    DIAMOND_A = ("♦", "A", 14)
    DIAMOND_2 = ("♦", "2", 15)

    # ── 大小王 ──
    SMALL_JOKER = ("🃏", "小王", 16)
    BIG_JOKER = ("🃟", "大王", 17)

    def __init__(self, symbol: str, rank: str, game_value: int):
        self.symbol = symbol
        self.rank = rank
        self.game_value = game_value

    def __lt__(self, other: "Card") -> bool:
        return self.game_value < other.game_value

    def __gt__(self, other: "Card") -> bool:
        return self.game_value > other.game_value

    @property
    def is_joker(self) -> bool:
        return self.game_value >= 16

    @property
    def is_red(self) -> bool:
        """♠♣ 为黑，♥♦ 为红。"""

        return self.symbol in ("♥", "♦")

    @classmethod
    def all_cards(cls) -> list["Card"]:
        """返回全部 54 张牌。"""

        return list(cls)

    def __repr__(self) -> str:
        return f"<{self.symbol}{self.rank}>"

def full_deck() -> list[Card]:
    """得到由所有牌组成的一副完整的牌"""
    return [c for c in Card]


