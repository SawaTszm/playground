import abc
from io import StringIO


class Builder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def make_title(self, title: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def make_string(self, string: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def make_items(self, items: list[str]) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def close(self) -> None:
        raise NotImplementedError()


class Director:
    def __init__(self, builder: Builder) -> None:
        self.builder = builder

    def construct(self) -> None:
        self.builder.make_title("Greeting")
        self.builder.make_string("朝から昼にかけて")
        self.builder.make_items(["おはよう", "こんにちは"])

        self.builder.make_string("夜に")
        self.builder.make_items(["こんばんは", "おやすみ", "さよなら"])
        self.builder.close()


class TextBuilder(Builder):
    def __init__(self) -> None:
        self.buffer = StringIO()

    def make_title(self, title: str) -> None:
        self.buffer.write("===========================\n")
        self.buffer.write(f"< {title} >\n\n")

    def make_string(self, string: str) -> None:
        self.buffer.write(f"◇{string}\n\n")

    def make_items(self, items: list[str]) -> None:
        for i in range(len(items)):
            self.buffer.write(f"  ・{items[i]}\n")
        self.buffer.write("\n")

    def close(self) -> None:
        self.buffer.write("===========================\n")

    def get_result(self) -> str:
        return self.buffer.getvalue()


class HTMLBuilder(Builder):
    def __init__(self) -> None:
        self.filename = ""

    def make_title(self, title: str) -> None:
        self.filename = f"{title}.html"
        self.buffer = open(self.filename, "w")

        self.buffer.write(f"<html><head><title>{title}</title></head><body>")
        self.buffer.write(f"<h1>{title}</h1>")

    def make_string(self, string: str) -> None:
        self.buffer.write(f"<p>{string}</p>")

    def make_items(self, items: list[str]) -> None:
        self.buffer.write("<ul>")
        for i in range(len(items)):
            self.buffer.write(f"<li>{items[i]}</li>")
        self.buffer.write("</ul>")

    def close(self) -> None:
        self.buffer.write("</body></html>")
        self.buffer.close()

    def get_result(self) -> str:
        return self.filename


if __name__ == '__main__':
    print("start:")
    print("textBuilder:")
    text_builder = TextBuilder()
    director = Director(text_builder)
    director.construct()
    result = text_builder.get_result()
    print(result)

    print("HTMLBuilder:")
    html_builder = HTMLBuilder()
    director = Director(html_builder)
    director.construct()
    result = html_builder.get_result()
    print(f"{result}が生成されました")
    print(":end")
