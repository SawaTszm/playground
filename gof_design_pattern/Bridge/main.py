import abc


class DisplayImpl(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def raw_open(self) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def raw_print(self) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def raw_close(self) -> None:
        raise NotImplementedError()


class Display:
    def __init__(self, impl: DisplayImpl) -> None:
        self.impl = impl

    def open(self):
        self.impl.raw_open()

    def print(self):
        self.impl.raw_print()

    def close(self):
        self.impl.raw_close()

    def display(self):
        self.open()
        self.print()
        self.close()


class CountDisplay(Display):
    def multi_display(self, times: int) -> None:
        self.open()
        for i in range(times):
            self.print()
        self.close()


class StringDisplayImpl(DisplayImpl):
    def __init__(self, string: str) -> None:
        self.string = string
        self.width = len(self.string)

    def raw_open(self) -> None:
        self.print_line()

    def raw_print(self) -> None:
        print(f"|{self.string}|")

    def raw_close(self) -> None:
        self.print_line()

    def print_line(self) -> None:
        print("+", end="")
        for i in range(self.width):
            print("-", end="")
        print("+")


if __name__ == '__main__':
    print("start:")
    d1 = Display(StringDisplayImpl("hello hoge!"))
    d2 = CountDisplay(StringDisplayImpl("hello huga!!"))
    d3 = CountDisplay(StringDisplayImpl("hello piyo!!!"))
    d1.display()
    d2.display()
    d3.display()
    d3.multi_display(5)
    print(":end")
