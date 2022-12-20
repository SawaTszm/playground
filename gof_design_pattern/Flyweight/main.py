class BigChar:
    def __init__(self, charname: str) -> None:
        self.charname = charname
        try:
            self.font_data = open(f"big{charname}.txt", "r").read()
        except Exception:
            self.font_data = "?"

    def print(self) -> None:
        print(self.font_data, end="")


class BigCharFactory:
    def __init__(self) -> None:
        self.pool: dict[str, BigChar] = {}

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "__instance__"):
            cls.__instance__ = super(BigCharFactory, cls).__new__(cls, *args, **kwargs)
        return cls.__instance__

    def get_big_char(self, charname: str) -> BigChar:
        bc = self.pool.get(charname, None)
        if not bc:
            bc = BigChar(charname)
            self.pool[charname] = bc
        return bc


class BigString:
    def __init__(self, string: str) -> None:
        self.bigchars: list[BigChar] = []
        self.bigchar_factories = BigCharFactory()
        for i in range(len(string)):
            self.bigchars.append(self.bigchar_factories.get_big_char(string[i]))

    def print(self) -> None:
        for i in range(len(self.bigchars)):
            self.bigchars[i].print()
        print("")

if __name__ == '__main__':
    print("start:")
    # 割愛してひらがなにしてます
    bs = BigString("1111-23")
    bs.print()
    print(":end")
