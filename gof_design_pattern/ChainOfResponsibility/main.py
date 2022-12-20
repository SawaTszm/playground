import abc
from typing import Any


class Trouble:
    def __init__(self, num: int) -> None:
        self.num = num

    def get_number(self) -> int:
        return self.num

    def to_string(self) -> str:
        return f"[Trouble {self.num}]"


class Support(metaclass=abc.ABCMeta):
    def __init__(self, name: str, *args: Any, ** kwargs: Any) -> None:
        self.name = name
        self.next = None

    def set_next(self, next: "Support") -> "Support":
        self.next = next
        return next

    def support(self, trouble: Trouble) -> None:
        if (self.resolve(trouble)):
            self.done(trouble)
        elif self.next != None:
            self.next.support(trouble)
        else:
            self.fail(trouble)

    def to_string(self) -> None:
        return f"[{self.name}]"

    @abc.abstractmethod
    def resolve(self, trouble: Trouble) -> bool:
        raise NotImplementedError()

    def done(self, trouble: Trouble) -> None:
        print(f"{trouble.to_string()} is resolved by {self.to_string()}.")

    def fail(self, trouble: Trouble) -> None:
        print(f"{trouble.to_string()} cannot be resolved.")


class NoSupport(Support):
    def resolve(self, trouble: Trouble) -> bool:
        return False


class LimitSupport(Support):
    def __init__(self, name: str, limit: int) -> None:
        super().__init__(name)
        self.limit = limit

    def resolve(self, trouble: Trouble) -> bool:
        if trouble.get_number() < self.limit:
            return True
        return False


class OddSupport(Support):
    def resolve(self, trouble: Trouble) -> bool:
        if trouble.get_number() % 2 == 1:
            return True
        return False


class SpecialSupport(Support):
    def __init__(self, name: str, num: int) -> None:
        super().__init__(name)
        self.num = num

    def resolve(self, trouble: Trouble) -> bool:
        if trouble.get_number() == self.num:
            return True
        return False


if __name__ == '__main__':
    print("start:")
    taro = NoSupport("taro")
    jiro = LimitSupport("jiro", 100)
    saburo = SpecialSupport("saburo", 429)
    shiro = LimitSupport("shiro", 200)
    goro = OddSupport("goro")
    mutsuro = LimitSupport("mutsuro", 300)
    taro.set_next(jiro).set_next(saburo).set_next(shiro).set_next(goro).set_next(mutsuro)
    for i in range(0, 500, 33):
        taro.support(Trouble(i))

    print(":end")
