import abc

# package command


class Command(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self) -> None:
        raise NotImplementedError()


class MacroCommand(Command):
    def __init__(self) -> None:
        self.commands: list[Command] = []

    def execute(self) -> None:
        for c in self.commands:
            c.execute()

    def append(self, cmd: Command) -> None:
        if (cmd != self):
            self.commands.append(cmd)

    def undo(self) -> None:
        self.commands.pop()

    def clear(self) -> None:
        self.commands.clear()


# package print

class PrintStringCommand(Command):
    def __init__(self, string: str) -> None:
        self.string = string

    def execute(self) -> None:
        print(self.string)


class PrintBorderCommand(Command):
    def __init__(self, size: int) -> None:
        self.size = size

    def execute(self) -> None:
        for i in range(self.size):
            print("=", end="")
        print("")


if __name__ == '__main__':
    print("start:")
    command = MacroCommand()
    s = PrintStringCommand("hogehugapiyo")
    b = PrintBorderCommand(12)
    command.append(b)
    command.append(s)
    command.append(b)
    command.execute()
    print(":end")
