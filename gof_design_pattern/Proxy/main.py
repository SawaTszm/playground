import abc
import time
from typing import Optional


class Printable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set_printer_name(self, name: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_print_name(self) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def print(self, string: str) -> None:
        raise NotImplementedError()


class Printer(Printable):
    def __init__(self, name: str) -> None:
        self.name = name
        self.heavy_job(f"Printerのインスタンス({name})を生成中")

    def set_printer_name(self, name: str) -> None:
        self.name = name

    def get_print_name(self) -> str:
        return self.name

    def print(self, string: str) -> None:
        print(f"==={self.name}===")
        print(string)

    def heavy_job(self, msg: str) -> None:
        print(msg, end="")
        for i in range(5):
            time.sleep(1)
            print(".", end="")
        print("done.")


class PrintProxy(Printable):
    def __init__(self, name: str) -> None:
        self.name = name
        self.real: Optional[Printer] = None

    def set_printer_name(self, name: str) -> None:
        self.name = name

        if self.real is not None:
            self.real.set_printer_name(name)

    def get_print_name(self) -> str:
        return self.name

    def print(self, string: str) -> None:
        self.realize()
        self.real.print(string)

    def realize(self) -> None:
        if self.real is None:
            self.real = Printer(self.name)


if __name__ == '__main__':
    print("start:")
    p = PrintProxy("hoge")
    print(f"名前は現在{p.get_print_name()}です")
    p.set_printer_name("huga")
    print(f"名前は現在{p.get_print_name()}です")
    p.print("Hello world!")
    print(":end")
