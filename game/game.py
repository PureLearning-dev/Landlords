import random

from cards.card import Card
from player.ai import AIPlayer
from player.base import BasePlayer
from player.type import Identity
from player.user import UserPlayer


class Game:
    """表示一局游戏"""

    NORMAL_NUM = 17

    SPECIAL_NUM = 3

    USER_NUM = 3

    BID_POINT_RULES = """
    
    游戏进入叫地主阶段，接下来需要确定出一名地主。
    
    规则：
        
        1. 玩家可以输入 1、2、3 中的一个值表达叫分分数，除此之外的任何输入都被视为跳过此次叫分
        2. 当前玩家叫分比上一个玩家叫分小的话，视为跳过
        3. 每名玩家有且只有一次叫分分数
        4. 只要有一名玩家叫分 3，则直接结束
        
    最终，叫分最大的玩家成为地主，身为地主，可以在 17 张普通牌的基础上，额外再多 3 张底牌。
    
    其余两名玩家为农民，视为联盟，需要共同战胜地主。
    
    获胜条件：哪一方首先打完手中的牌，则那一方获胜！
        
    """

    CALL_LANDLORD_PROMPT = '请输入你的叫分：'

    def __init__(self, cards: list[Card], users: list[BasePlayer]):
        """
        :param cards: 一局游戏的初始化牌
        :param users: 一局游戏的玩家
        """

        self.cards = cards
        self.users = users

    def _shuffle(self):
        random.shuffle(self.cards)

    def _deal_normal_cards(self):
        for i in range(self.USER_NUM):
            start = i * self.NORMAL_NUM
            end = (i + 1) * self.NORMAL_NUM
            self.users[i].normal_cards = self.cards[start:end]

    def _reset_players(self):
        for user in self.users:
            user.normal_cards = []
            user.special_cards = []
            user.identity = None

    def call_the_landlord(self) -> None:
        print(self.BID_POINT_RULES)

        def assign_player_identity(users, landlord_index):
            for user_index, user in enumerate(users):
                user.identity = Identity.LANDOWNER if user_index == landlord_index else Identity.FARMER

        while True:
            cur_user = random.randint(0, self.USER_NUM - 1)
            max_point_info = {'max_point': 0, 'landlord_index': -1}
            i = 0
            has_landlord = False

            while i < 3:
                cur_player = self.users[cur_user]

                if isinstance(cur_player, UserPlayer):
                    print(f"{cur_user + 1} 号玩家-[人类玩家]，名称为 {cur_player.name}")
                elif isinstance(cur_player, AIPlayer):
                    print(f"{cur_user + 1} 号玩家-[AI玩家]，名称为 AI")

                cur_point = input(self.CALL_LANDLORD_PROMPT)
                result = self.users[cur_user].call_the_landlord(max_point_info['max_point'], cur_point)

                if result == 0:
                    i += 1
                    cur_user = (cur_user + 1) % self.USER_NUM
                    continue
                elif result == 1:
                    max_point_info['max_point'] = int(cur_point)
                    max_point_info['landlord_index'] = cur_user
                    has_landlord = True
                elif result == 2:
                    max_point_info['max_point'] = 3
                    max_point_info['landlord_index'] = cur_user
                    has_landlord = True
                    break

                cur_user = (cur_user + 1) % self.USER_NUM
                i += 1

            if not has_landlord:
                self.redeal()
                continue

            landlord_user = self.users[max_point_info['landlord_index']]
            if isinstance(landlord_user, UserPlayer):
                print(f"{landlord_user.name} 成功获得地主，当前 max_point 值为 {max_point_info['max_point']}")
            assign_player_identity(self.users, max_point_info['landlord_index'])
            break

    def redeal(self):
        """重发牌，用于没人叫地主时重新开始"""
        print("所有玩家都跳过叫分，重新洗牌发牌并叫地主...")
        self._reset_players()
        self._shuffle()
        self._deal_normal_cards()

    def assign_player_normal_cards(self, cards: list[Card]):
        """给玩家分配普通牌"""
        # 给每个玩家分配牌
        for i in range(3):
            normal_cards = cards[i * self.NORMAL_NUM : (i + 1) * self.NORMAL_NUM]
            self.users[i].normal_cards = normal_cards

    def assign_player_special_cards(self, cards: list[Card]) -> list[Card]:
        """给玩家分配底牌"""
        special_cards = cards[51 : 54]

        for user in self.users:
            if user.identity == Identity.LANDOWNER:
                user.special_cards = special_cards

        return special_cards

    def init_all_data(self):
        print(f"没有打乱的牌有 {len(self.cards)} 张，如下：")
        print(self.cards)

        self._shuffle()
        print(f"打乱的牌有 {len(self.cards)} 张，如下：")
        print(self.cards)

        print("每个玩家分配 17 张普通牌")
        self._deal_normal_cards()
        for user in self.users:
            print(user.show_normol_cards())

        self.call_the_landlord()

        special_cards = self.assign_player_special_cards(self.cards)
        print(f"底牌有 {len(special_cards)} 张，如下：")
        print(special_cards)




