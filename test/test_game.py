from cards.card import full_deck, Card
from player.type import Identity
from player.user import UserPlayer
from game.game import Game

class TestGame:

    def __init__(self, users: list[UserPlayer] | None = None,
                 cards: list[Card] | None = None):
        self.users = users or []
        self.cards = cards or []
        self.game = Game(self.cards, self.users)

    def test_game_data(self):
        print("一副牌中包含的内容：")
        print(self.game.cards)
        print("参与游戏的初始化玩家：")
        print(self.game.users)

    def test_game_process(self):
        self.game.init_all_data()

        print(f"{'-' * 40} 当前不同玩家拥有的信息 {'-' * 40}")
        for index, user in enumerate(self.users):
            print(f"玩家 {index}：{user.name} 的角色是 【{user.identity.value}】")
            print(f"玩家 {index}：{user.name} 的手牌有 {user.hold_cards}")
            if user.identity == Identity.LANDOWNER:
                print(f"{'-' * 40} [{user.name}]是地主 {'-' * 40}")
                print(f"手牌中包括普通牌：{user.normal_cards}")
                print(f"和底牌 {user.special_cards}")


def init_users(users: list[UserPlayer] | None = None):
    if users is None:
        users: list[UserPlayer] = []
    user1 = UserPlayer("龚媛", 21)
    user2 = UserPlayer("刘杰", 22)
    user3 = UserPlayer("刘寅坤", 19)
    users.append(user1)
    users.append(user2)
    users.append(user3)
    return users

def my_print(content):
    print(f"{'-' * 40} 测试：{content} {'-' * 40}")

if __name__ == "__main__":
    test = TestGame(init_users(), full_deck())
    my_print("游戏中的数据")
    test.test_game_data()
    my_print("叫地主和分牌")
    test.test_game_process()