from cards.card import Card, full_deck


def test_card():
    cards = full_deck()

    # 枚举类中定义的枚举是该类的一个实例
    # 遍历类，会将实例组成一个 list 使用
    for _ in cards:
        print(_.__repr__())

test_card()
