import abc


class Display(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_columns(self) -> int:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_rows(self) -> int:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_row_text(self, row: int) -> str:
        raise NotImplementedError()

    def show(self) -> None:
        for i in range(self.get_rows()):
            print(self.get_row_text(i))


class StringDisplay(Display):
    def __init__(self, string: str) -> None:
        self.string = string

    def get_columns(self) -> int:
        return len(self.string)

    def get_rows(self) -> int:
        return 1

    def get_row_text(self, row: int) -> str:
        if row == 0:
            return self.string
        return ""


class Border(Display, metaclass=abc.ABCMeta):
    def __init__(self, display: Display) -> None:
        self.display = display


class SideBorder(Border):
    def __init__(self, display: Display, ch: str) -> None:
        super().__init__(display)
        self.border_char = ch

    def get_columns(self) -> int:
        return self.display.get_columns() + 2

    def get_rows(self) -> int:
        return self.display.get_rows()

    def get_row_text(self, row: int) -> str:
        return f"{self.border_char}{self.display.get_row_text(row)}{self.border_char}"


class FullBorder(Border):
    def get_columns(self) -> int:
        return self.display.get_columns() + 2

    def get_rows(self) -> int:
        return self.display.get_rows() + 2

    def get_row_text(self, row: int) -> str:
        if row == 0:
            return f"+{'-' * self.display.get_columns()}+"
        elif row == (self.display.get_rows() + 1):
            return f"+{'-' * self.display.get_columns()}+"
        else:
            return f"|{self.display.get_row_text(row - 1)}|"


if __name__ == '__main__':
    print("start:")
    d1 = StringDisplay("Hello, world!")
    d2 = SideBorder(d1, "#")
    d3 = FullBorder(d2)
    d1.show()
    d2.show()
    d3.show()

    d4 = (
        SideBorder(
            FullBorder(
                FullBorder(
                    SideBorder(
                        FullBorder(
                            StringDisplay("Hello.")
                        ), "*"
                    )
                )
            ), "/"
        )
    )
    d4.show()
    print(":end")
