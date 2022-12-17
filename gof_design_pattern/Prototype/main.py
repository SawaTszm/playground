import abc
from copy import copy
from typing import Any

# package framework


class Product(metaclass=abc.ABCMeta):
    """複製可能な製品の抽象クラス"""
    @abc.abstractmethod
    def use(self, *args: Any, **kwargs: Any) -> None:
        # TIL: *args: Any, **kwargs: Anyで宣言しておけば継承先で引数を追加できる
        raise NotImplementedError()

    @abc.abstractmethod
    def createClone(self, *args: Any, **kwargs: Any) -> 'Product':
        # TIL: 自身の型を返す時に文字列定義にすると型解釈で怒られない
        raise NotImplementedError()


class Manager:
    """prototypeを管理するManagerクラス"""
    def __init__(self) -> None:
        self.showcase: dict[str, Product] = {}

    def register(self, name: str, proto: Product) -> None:
        self.showcase[name] = proto

    def create(self, protoname: str) -> Product:
        p = self.showcase.get(protoname)
        if p:
            return p.createClone()
        else:
            raise Exception


# no package

class MessageBox(Product):
    def __init__(self, decochar: str) -> None:
        self.decochar = decochar

    def use(self, s: str) -> None:
        length = len(s)
        for i in range(length + 4):
            print(self.decochar, end="")
        print("")
        print(f"{self.decochar} {s} {self.decochar}")
        for i in range(length + 4):
            print(self.decochar, end="")
        print("")

    def createClone(self) -> 'Product':
        return copy(self)


class UnderlinePen(Product):
    def __init__(self, unchar: str) -> None:
        self.unchar = unchar

    def use(self, s: str) -> None:
        length = len(s)
        print(f"\"{s}\"")
        print(" ", end="")
        for i in range(length):
            print(self.unchar, end="")
        print(" ")

    def createClone(self) -> 'Product':
        return copy(self)


if __name__ == '__main__':
    print("start:")
    # 準備
    manager = Manager()
    upen = UnderlinePen("~")
    mbox = MessageBox("*")
    sbox = MessageBox("/")
    manager.register("strong message", upen)
    manager.register("warning box", mbox)
    manager.register("slash box", sbox)

    # 描画
    p1 = manager.create("strong message")
    p1.use("Hello, world.")
    p2 = manager.create("warning box")
    p2.use("Hello, world.")
    p3 = manager.create("slash box")
    p3.use("Hello, world.")
    print(":end")
