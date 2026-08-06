import random

from cards.card import Card
from player.base import BasePlayer
from player.type import Identity


class Game:
    """表示一局游戏"""

    NORMAL_NUM = 17

    SPECIAL_NUM = 3

    USER_NUM = 3

    CALL_LANDLORD_PROMPT = '请输入你的叫分，你只有这一次叫分机会，可以输入 1、2、3，除此之外的输入被视为跳过这次叫分，注意：当输入的值小于前面用户的叫分时，也视为跳过'

    def __init__(self, cards: list[Card], users: list[BasePlayer]):
        """
        :param cards: 一局游戏的初始化牌
        :param users: 一局游戏的玩家
        """

        self.cards = cards
        self.users = users

    def call_the_landlord(self) -> None:
        """
        叫地主阶段

        :return: 地主玩家的下标（编号：0、1、2）
        """

        def assign_player_identity(users: list[BasePlayer], landlord_index: int):
            for index, user in enumerate(users):
                if index == landlord_index:
                    user.identity = Identity.LANDOWNER
                else:
                    user.identity = Identity.LANDOWNER

        cur_user = random.randint(0, self.USER_NUM - 1)

        max_point_info = {
            'max_point':  0,
            'landlord_index': -1
        }

        i = 0

        # 从 cur_user 开始叫分，每个玩家最多有一次机会
        # 得到地主是谁
        while i < 3:
            cur_point = input(self.CALL_LANDLORD_PROMPT)
            result = self.users[cur_user].call_the_landlord(max_point_info['max_point'], cur_point)

            if result == 0:
                break
            elif result == 1:
                max_point_info['landlord_index'] = cur_user
                break
            elif result == 2:
                continue
            else:
                max_point_info['max_point'] = int(cur_point)
                max_point_info['landlord_index']  = cur_user

            cur_user = (cur_user + 1) % self.USER_NUM
            i += 1

        # 分配玩家角色
        assign_player_identity(users=self.users, landlord_index=max_point_info['landlord_index'])

    def assign_player_normal_cards(self, cards: list[Card]):
        # 打乱牌排序
        random.shuffle(cards)

        # 给每个用户分配牌
        for i in range(3):
            normal_cards = cards[i * self.NORMAL_NUM : (i + 1) * self.NORMAL_NUM]
            self.users[i].normal_cards = normal_cards

    def assign_player_special_cards(self, cards: list[Card]):
        special_cards = cards[54 : 57]
        for user in self.users:
            if user.identity == Identity.LANDOWNER:
                user.special_cards = special_cards

    def init_all_data(self):
        """
        组装得到的数据，初始化整局游戏的数据

        :return: None
        """

        # 得到一副打乱的牌
        random.shuffle(self.cards)

        # 给每个用户 17 张普通牌
        self.assign_player_normal_cards(cards=self.cards)

        # 叫地主
        self.call_the_landlord()

        # 给地主 3 张底牌
        self.assign_player_special_cards(cards=self.cards)




