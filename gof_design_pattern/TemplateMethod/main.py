import abc


# TIL: end=None で改行が消せる(デフォルトが\nだから改行する)
def print_wo_new_line(data: str) -> None:
    print(data, end="")


class AbstractDisplay(metaclass=abc.ABCMeta):
    """具体的な処理を継承先に任せる抽象クラス"""

    @abc.abstractmethod
    def open(self) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def print(self) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def close(self) -> None:
        raise NotImplementedError()

    def display(self) -> None:
        self.open()
        for i in range(5):
            self.print()
        self.close()


class CharDisplay(AbstractDisplay):
    """open,print,closeの具体的な実装をしたクラス①"""
    def __init__(self, char: str) -> None:
        self.char = char

    def open(self) -> None:
        print_wo_new_line("<<")

    def print(self) -> None:
        print_wo_new_line(self.char)

    def close(self) -> None:
        print(">>")


class TextDisplay(AbstractDisplay):
    """open,print,closeの具体的な実装をしたクラス②"""
    def __init__(self, text: str) -> None:
        self.text = text
        self.length = len(self.text)

    def print_line(self) -> None:
        print_wo_new_line("+")
        for i in range(self.length):
            print_wo_new_line("-")
        print("+")

    def open(self) -> None:
        self.print_line()

    def print(self) -> None:
        print(f"|{self.text}|")

    def close(self) -> None:
        self.print_line()


if __name__ == '__main__':
    print("start:")
    char = CharDisplay("H")
    txt = TextDisplay("Hello, world.")
    char.display()
    txt.display()
    print(":end")
