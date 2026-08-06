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

    def call_the_landlord(self) -> None:
        """
        叫地主流程

        随机获取第一位叫地主的玩家，顺时针叫分，如果叫分小于当前最大叫分，则视为跳过，如果不是输入的 1、2、3，也视为跳过

        叫分最大的玩家为地主
        """

        # 随机抽取一名玩家先叫地主
        cur_user = random.randint(0, self.USER_NUM - 1)

        # 场上的最大分数和当前的地主玩家下标
        max_point_info = {
            'max_point': 0,
            'landlord_index': -1
        }

        # 更新玩家的身份
        def assign_player_identity(users: list[BasePlayer], landlord_index: int):
            for user_index, user in enumerate(users):
                if user_index == landlord_index:
                    user.identity = Identity.LANDOWNER
                else:
                    user.identity = Identity.FARMER

        i = 0
        landlord_flag = 0

        print(self.BID_POINT_RULES)
        # 从 cur_user 开始叫分，每个玩家最多有一次机会
        # 最多轮转 3 次
        while i < 3:
            # 得到第一个叫分的玩家
            cur_player: BasePlayer = self.users[cur_user]

            # 判断玩家是 AI 还是真人
            # 输出当前玩家的基础信息
            if isinstance(cur_player, UserPlayer):
                print(f"{self.users.index(cur_player) + 1} 号玩家-[人类玩家]，名称为 {cur_player.name}")
            elif isinstance(cur_player, AIPlayer):
                print(f"[AI玩家]，名称为 AI")

            # 获取当前玩家叫的内容
            cur_point: str = input(self.CALL_LANDLORD_PROMPT)

            # 输出当前玩家叫分的信息，并执行叫分后的逻辑
            result = self.users[cur_user].call_the_landlord(max_point_info['max_point'], cur_point)

            if result == 0:
                i += 1
                cur_user = (cur_user + 1) % self.USER_NUM
                continue
            elif result == 1:
                max_point_info['max_point'] = int(cur_point)
                max_point_info['landlord_index'] = cur_user
                if landlord_flag == 0:
                    landlord_flag = 1
            elif result == 2:
                max_point_info['max_point'] = 3
                max_point_info['landlord_index'] = cur_user
                if landlord_flag == 0:
                    landlord_flag = 1
                break

            cur_user = (cur_user + 1) % self.USER_NUM
            i += 1

        # 判断是否确定了地主，如果没有确定，则随机确定一个玩家为地主
        if landlord_flag == 0:
            max_point_info['landlord_index'] = random.randint(0, self.USER_NUM - 1)
            print("所有玩家都跳过叫分，随意随机确定一名地主")

        # 输出最终得到的地主信息
        landlord_user = self.users[max_point_info['landlord_index']]
        if isinstance(landlord_user, UserPlayer):
            print(f"{landlord_user.name} 成功获得地主，当前 max_point 值为 {max_point_info['max_point']}")

        # 分配玩家角色
        assign_player_identity(users=self.users, landlord_index=max_point_info['landlord_index'])

    def assign_player_normal_cards(self, cards: list[Card]):
        # 给每个用户分配牌
        for i in range(3):
            normal_cards = cards[i * self.NORMAL_NUM : (i + 1) * self.NORMAL_NUM]
            self.users[i].normal_cards = normal_cards

    def assign_player_special_cards(self, cards: list[Card]) -> list[Card]:
        special_cards = cards[51 : 54]

        for user in self.users:
            if user.identity == Identity.LANDOWNER:
                user.special_cards = special_cards

        return special_cards

    def init_all_data(self):
        """
        组装得到的数据，初始化整局游戏的数据

        :return: None
        """
        print(f"没有打乱的牌有 {len(self.cards)} 张，如下：")
        print(self.cards)

        # 得到一副打乱的牌
        random.shuffle(self.cards)
        print(f"打乱的牌有 {len(self.cards)} 张，如下：")
        print(self.cards)

        # 给每个用户 17 张普通牌
        print("每个玩家分配 17 张普通牌")
        self.assign_player_normal_cards(cards=self.cards)
        for user in self.users:
            user_normal_cards = user.show_normol_cards()
            print(user_normal_cards)

        # 叫地主
        self.call_the_landlord()

        # 给地主 3 张底牌
        special_cards = self.assign_player_special_cards(cards=self.cards)
        print(f"底牌有 {len(special_cards)} 张，如下：")
        print(special_cards)




