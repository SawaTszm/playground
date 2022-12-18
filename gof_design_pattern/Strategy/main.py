import abc


class Hand:
    HANDVALUE_GUU = 0
    HANDVALUE_CHO = 1
    HANDVALUE_PAA = 2
    hand: dict[int, "Hand"] = {}
    name = ["グー", "チョキ", "パー"]

    def __init__(self, hand_value: int) -> None:
        self._hand_value = hand_value

    @classmethod
    def get_hand(cls, hand_value: int) -> "Hand":
        return cls.hand[hand_value]

    def is_stronger_than(self, h: "Hand"):
        return self.fight(h) == 1

    def isWeakerThan(self, h: "Hand"):
        return self.fight(h) == -1

    def fight(self, h: "Hand"):
        if self == h:
            return 0
        elif (self._hand_value + 1) % 3 == h._hand_value:
            return 1
        else:
            return -1


class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def hext_hand(self) -> Hand:
        raise NotImplementedError()

    @abc.abstractmethod
    def study(self, win: bool) -> None:
        raise NotImplementedError()


class WinningStrategy(Strategy):
    def __init__(self, seed: int) -> None:
        # TODO: 途中！！！！！
        pass
