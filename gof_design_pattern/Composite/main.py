import abc
from typing import Any


class Entry(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_name(self, *args: Any, **kwargs: Any) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_size(self, *args: Any, **kwargs: Any) -> int:
        raise NotImplementedError()

    def add(self, entry: "Entry") -> "Entry":
        # 実装されていないサブクラスは自身に追加ができない
        # e.g.ディレクトリはaddできるけどファイルはaddできない
        raise NotImplementedError()

    def print_all(self) -> None:
        self.print_list("")

    @abc.abstractmethod
    def print_list(self, prefix: str) -> None:
        raise NotImplementedError()

    def __str__(self) -> str:
        return f"{self.get_name()} ({self.get_size()})"


class File(Entry):
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> str:
        return self.size

    def print_list(self, prefix: str) -> None:
        print(f"{prefix}/{self}")


class Directory(Entry):
    def __init__(self, name: str) -> None:
        self.name = name
        self.directory = []

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        size = 0
        for entry in self.directory:
            size += entry.get_size()
        return size

    def add(self, entry: Entry) -> Entry:
        self.directory.append(entry)
        return self

    def print_list(self, prefix: str = "") -> None:
        print(f"{prefix}/{self}")
        for entry in self.directory:
            entry.print_list(f"{prefix}/{self.name}")


if __name__ == '__main__':
    print("start:")
    print("root entryを作ります")
    rootdir = Directory("root")
    bindir = Directory("bin")
    tmpdir = Directory("tmp")
    usrdir = Directory("usr")
    rootdir.add(bindir)
    rootdir.add(tmpdir)
    rootdir.add(usrdir)
    bindir.add(File("vi", 10000))
    bindir.add(File("latex", 20000))
    rootdir.print_list()

    print("")
    print("user entryを作ります")
    hoge = Directory("hoge")
    huga = Directory("huga")
    piyo = Directory("piyo")
    usrdir.add(hoge)
    usrdir.add(huga)
    usrdir.add(piyo)
    hoge.add(File("diary.html", 100))
    hoge.add(File("composite.python", 200))
    huga.add(File("memo.txt", 300))
    piyo.add(File("game.doc", 400))
    piyo.add(File("piyo.mail", 500))
    rootdir.print_list()
    print(":end")
