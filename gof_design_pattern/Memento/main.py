import copy
import random
import time


class Memento:
    def __init__(self, money: int) -> None:
        self.money = money
        self.fruits: list[str] = []

    def get_money(self) -> int:
        return self.money

    def add_fruit(self, fruit: str) -> None:
        self.fruits.append(fruit)

    def get_fruites(self) -> list[str]:
        return copy.copy(self.fruits)


class Gamer:
    def __init__(self, money: int) -> None:
        self.money = money
        self.fruits: list[str] = []
        self.fruits_name = [
            "りんご", "ぶどう", "バナナ", "みかん",
        ]

    def get_money(self) -> int:
        return self.money

    def bet(self) -> None:
        dice = random.randint(1,6)
        if dice == 1:
            self.money += 100
            print("所持金が増えました！")
        elif dice == 2:
            self.money /= 2
            print("所持金が半分になりました……")
        elif dice == 6:
            f = self.get_fruit()
            print(f"フルーツ: {f}をもらいました！")
            self.fruits.append(f)
        else:
            print("何も起こりませんでした。")

    def create_memento(self) -> Memento:
        m = Memento(self.money)
        for f in self.fruits:
            if f.startswith("おいしい"):
                # フルーツは美味しいものだけ保存する
                m.add_fruit(f)
        return m

    def restore_memento(self, memento: Memento) -> None:
        self.money = memento.money
        self.fruits = memento.get_fruites()

    def __str__(self) -> str:
        return f"[money = {self.money}, fruites = {self.fruits}]"

    def get_fruit(self) -> str:
        prefix = ""
        if random.randint(0,1):
            prefix = "おいしい"
        return f"{prefix}{self.fruits_name[random.randint(0, len(self.fruits_name) - 1)]}"


if __name__ == '__main__':
    print("start:")
    gamer = Gamer(100)
    memento = gamer.create_memento()
    for i in range(100):
        print(f"==== {i}")
        print(f"現状: {gamer}")

        gamer.bet()

        print(f"所持金は{gamer.get_money()}円になりました")

        # Mementoの取り扱いの決定
        if gamer.get_money() > memento.get_money():
            print("    （お金が増えたので、現在の状態を保存しておこう）")
            memento = gamer.create_memento()
        elif gamer.get_money() < (memento.get_money() / 2):
            print("    （お金が結構減ったので、以前の状態に復帰しよう）")
            gamer.restore_memento(memento)
        print("")
        time.sleep(0.5)
    print(":end")
