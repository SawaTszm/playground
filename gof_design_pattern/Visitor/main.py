import abc
from functools import singledispatchmethod
from typing import Any


class Element(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def accept(self, v: "Visitor") -> None:
        raise NotImplementedError()


class Entry(Element, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_size(self) -> int:
        raise NotImplementedError()

    def add(self, entry: "Entry"):
        raise Exception()

    def to_string(self) -> str:
        return f"{self.get_name()}({self.get_size()})"


class File(Entry):
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        return self.size

    def accept(self, v: "Visitor") -> None:
        v.visit(self)


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

    def accept(self, v: "Visitor") -> None:
        v.visit(self)


class Visitor(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def visit(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError()


class ListVisitor(Visitor):
    def __init__(self) -> None:
        self.currentdir = ""

    # TIL: オーバーロードを実現するための組み込み in functools
    # classmethodやstaticmethodはsingledispatch,
    # 第一引数にselfが入る通常のmethodはsingledispatchmethodを使う。
    @singledispatchmethod
    def visit(self, file: "File") -> None:
        print(f"{self.currentdir}/{file.to_string()}")

    @visit.register
    def _(self, directory: "Directory") -> None:
        print(f"{self.currentdir}/{directory.to_string()}")
        savedir = self.currentdir
        self.currentdir = f"{self.currentdir}/{directory.get_name()}"
        for entry in directory.directory:
            entry.accept(self)
        self.currentdir = savedir


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
    rootdir.accept(ListVisitor())

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
    rootdir.accept(ListVisitor())
    print(":end")
