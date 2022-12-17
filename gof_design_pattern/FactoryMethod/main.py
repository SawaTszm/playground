import abc
import typing


# package framework

class Product(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def use(self) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_owner(self) -> str:
        # 本の内容にはない: IdCardのドメインなのでここに書かない方が良さそう
        # ただ、IdCardFactory.register_product()でget_owner()するときに怒られるので追加
        # 別の回避方法がありそう
        raise NotImplementedError()


class Factory(metaclass=abc.ABCMeta):
    def create(self, owner: str) -> Product:
        p = self.create_product(owner)
        self.register_product(p)
        return p

    @abc.abstractmethod
    def create_product(self, owner: str) -> Product:
        raise NotImplementedError()

    @abc.abstractmethod
    def register_product(self, product: Product) -> None:
        raise NotImplementedError()


# package idcard

class IdCard(Product):
    def __init__(self, owner: str) -> None:
        print(f"{owner}のカードを作ります:")
        self.owner = owner

    def use(self) -> None:
        print(f"{self.owner}のカードを使います:")

    def get_owner(self) -> str:
        return self.owner


class IdCardFactory(Factory):
    def __init__(self) -> None:
        self.owners: typing.List[str] = []

    def create_product(self, owner: str) -> Product:
        return IdCard(owner)

    def register_product(self, product: Product) -> None:
        self.owners.append(product.get_owner())


if __name__ == '__main__':
    print("start:")
    factory = IdCardFactory()
    card1 = factory.create("ほげ太郎")
    card2 = factory.create("ふが次郎")
    card3 = factory.create("ぴよ三郎")
    card1.use()
    card2.use()
    card3.use()
    print(":end")
