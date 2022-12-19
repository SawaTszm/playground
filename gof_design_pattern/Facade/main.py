from configparser import ConfigParser, SectionProxy
from io import TextIOWrapper


class Database:
    def __init__(self) -> None:
        # インスタンス生成はエラーにする
        raise Exception()

    @staticmethod
    def get_properties(dbname: str) -> SectionProxy:
        filename = f"{dbname}.ini"
        # JavaのProterties()をConfigParserで代用
        conf = ConfigParser()
        try:
            conf.read(filename)
        except Exception:
            print(f"Warning: [{filename}] is not found.")
        return conf[dbname]


class HtmlWriter:
    def __init__(self, writer: TextIOWrapper) -> None:
        self.writer = writer

    def title(self, title: str):
        self.writer.write("<html>")
        self.writer.write("<head>")
        self.writer.write(f"<title>{title}</title>")
        self.writer.write("</head>")
        self.writer.write("<body>\n")
        self.writer.write(f"<h1>{title}</h1>\n")

    def paragraph(self, msg: str) -> None:
        self.writer.write(f"<p>{msg}</p>\n")

    def link(self, href: str, caption: str) -> None:
        self.paragraph(f"<a href=\"{href}\">{caption}</a>")

    def mailto(self, mailaddr: str, username: str) -> None:
        self.link(f"mailto:{mailaddr}", username)

    def close(self) -> None:
        self.writer.write("</body>")
        self.writer.write("</html>\n")
        self.writer.close()


class PageMaker:
    def __init__(self) -> None:
        # インスタンス生成はエラーにする
        raise Exception()

    @staticmethod
    def make_welcome_page(mailaddr: str, filename: str) -> None:
        mailprop = Database.get_properties("maildata")
        username = mailprop[mailaddr]
        writer = HtmlWriter(open(filename, "w"))
        writer.title(f"Welcome to {username}'s page!")
        writer.paragraph(f"{username}のページへようこそ！")
        writer.paragraph("メール待ってますね。")
        writer.mailto(mailaddr, username)
        writer.close()
        print(f"{filename} is created for {mailaddr}{(username)}")


if __name__ == '__main__':
    print("start:")
    PageMaker.make_welcome_page("hoge@hoge.com", "welcome.html")
    print(":end")
