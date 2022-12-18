import abc
from typing import Any
from io import StringIO

# package factory


class Item(metaclass=abc.ABCMeta):
    def __init__(self, caption: str, *args: Any, **kwargs: Any) -> None:
        self._caption = caption

    @abc.abstractmethod
    def make_html(self) -> str:
        raise NotImplementedError()


class Link(Item, metaclass=abc.ABCMeta):
    def __init__(self, caption: str, url: str, *args: Any, **kwargs: Any) -> None:
        super().__init__(caption)
        self._url = url


class Tray(Item, metaclass=abc.ABCMeta):
    def __init__(self, caption: str, *args: Any, **kwargs: Any) -> None:
        super().__init__(caption)
        self._tray: list[Item] = []

    def add(self, item: Item):
        self._tray.append(item)


class Page(metaclass=abc.ABCMeta):
    def __init__(self, title: str, author: str, *args: Any, **kwargs: Any) -> None:
        self._title = title
        self._author = author
        self._content: list[Item] = []

    def add(self, item: Item) -> None:
        self._content.append(item)

    def output(self) -> None:
        filename = f"{self._title}.html"
        writer = open(filename, "w")
        writer.write(self.make_html())
        writer.close()
        print(f"{filename}を作成しました")

    @abc.abstractmethod
    def make_html(self) -> str:
        raise NotImplementedError()


class Factory(metaclass=abc.ABCMeta):
    @staticmethod
    def get_factory(classname: str) -> "Factory":
        try:
            return globals()[classname]()
        except Exception:
            print(f"{classname}が見つかりません")
            raise Exception()

    @abc.abstractmethod
    def create_link(self, caption: str, url: str) -> Link:
        raise NotImplementedError()

    @abc.abstractmethod
    def create_tray(self, caption: str) -> Tray:
        raise NotImplementedError()

    @abc.abstractmethod
    def create_page(self, title: str, author: str) -> Page:
        raise NotImplementedError()


# package listfactory

class ListFactory(Factory):
    def create_link(self, caption: str, url: str) -> Link:
        return ListLink(caption, url)

    def create_tray(self, caption: str) -> Tray:
        return ListTray(caption)

    def create_page(self, title: str, author: str) -> Page:
        return ListPage(title, author)


class ListLink(Link):
    def __init__(self, caption: str, url: str) -> None:
        super().__init__(caption, url)

    def make_html(self) -> str:
        return f"  <li><a herf=\"{self._url}\">{self._caption}</a></li>\n"


class ListTray(Tray):
    def __init__(self, caption: str) -> None:
        super().__init__(caption)

    def make_html(self) -> str:
        buffer = StringIO()
        buffer.write("<li>\n")
        buffer.write(f"{self._caption}\n")
        buffer.write("<ul>\n")
        for item in self._tray:
            buffer.write(item.make_html())
        buffer.write("</ul>\n")
        buffer.write("</li>\n")
        return buffer.getvalue()


class ListPage(Page):
    def __init__(self, title: str, author: str) -> None:
        super().__init__(title, author)

    def make_html(self) -> str:
        buffer = StringIO()
        buffer.write(f"<html><head><title>{self._title}</title></head>\n")
        buffer.write("<body>\n")
        buffer.write(f"<h1>{self._title}</h1>\n")
        buffer.write("<ul>\n")
        for item in self._content:
            buffer.write(item.make_html())
        buffer.write("</ul>\n")
        buffer.write(f"<hr><address>{self._author}</address>")
        buffer.write("</body></html>\n")
        return buffer.getvalue()


# 省略: TableFactory


if __name__ == '__main__':
    print("start:")
    factory = Factory.get_factory("ListFactory")

    hoge = factory.create_link("ほげ新聞", "<何かしらのURL1>")
    huga = factory.create_link("ふが新聞", "<何かしらのURL2>")
    piyo = factory.create_link("ぴよWeb", "<何かしらのURL3>")

    tray_news = factory.create_tray("新聞")
    tray_news.add(hoge)
    tray_news.add(huga)

    tray_serach = factory.create_tray("サーチエンジン(Web)")
    tray_serach.add(piyo)

    page = factory.create_page("Link page", "Sawa")
    page.add(tray_news)
    page.add(tray_serach)

    page.output()
    print(":end")
