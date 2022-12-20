import abc
import random
import time


class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, generator: "NumberGenerator") -> None:
        raise NotImplementedError()


class NumberGenerator(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        self.observers: list[Observer] = []

    def add_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def delete_observer(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify_observers(self) -> None:
        for o in self.observers:
            o.update(self)

    @abc.abstractmethod
    def get_number(self) -> int:
        raise NotImplementedError()

    @abc.abstractmethod
    def execute(self) -> None:
        raise NotImplementedError()


class RandomNumberGenerator(NumberGenerator):
    def __init__(self) -> None:
        super().__init__()
        self.num = 0

    def get_number(self) -> int:
        return self.num

    def execute(self) -> None:
        for i in range(5):
            self.num = random.randint(0, 50)
            self.notify_observers()


class DigitObserver(Observer):
    def update(self, generator: "NumberGenerator") -> None:
        print(f"DigitObserver: {generator.get_number()}")
        time.sleep(1)  # 表示がわかりやすいように少し時間を止めているだけ


class GraphObserver(Observer):
    def update(self, generator: "NumberGenerator") -> None:
        print("GraphObserver: ", end="")
        count = generator.get_number()
        for c in range(count):
            print("*", end="")
        print("")
        time.sleep(1)


if __name__ == '__main__':
    print("start:")
    g = RandomNumberGenerator()
    o1 = DigitObserver()
    o2 = GraphObserver()
    g.add_observer(o1)
    g.add_observer(o2)
    g.execute()
    print(":end")
