import abc
from typing import Optional


class Context:
    def __init__(self, text: str) -> None:
        self.list = text.split(" ")
        self.index = 0
        self.next_token()

    def next_token(self) -> str:
        if len(self.list) == self.index:
            self.current_token = None
        else:
            self.current_token = self.list[self.index]
            self.index += 1
        return str(self.current_token)

    def get_str_current_token(self) -> str:
        return str(self.current_token) or ""

    def skip_token(self, token: str) -> None:
        if (token != self.current_token):
            raise Exception()
        self.next_token()

    def current_number(self) -> str:
        return self.current_token or ""


class Node(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def parse(self, context: Context) -> None:
        raise NotImplementedError()

    def to_string(self) -> str:
        return ""


class RepeatCommandNode(Node):
    def parse(self, context: Context) -> None:
        context.skip_token("repeat")
        self.number = context.current_number()
        context.next_token()
        self.command_list_node = CommandListNode()
        self.command_list_node.parse(context)

    def to_string(self) -> str:
        return f"[repeat {self.number} {self.command_list_node.to_string()}]"


class PrimitiveCommandNode(Node):
    def parse(self, context: Context) -> None:
        self.name = context.get_str_current_token()
        context.skip_token(self.name)
        if self.name not in ["go", "right", "left"]:
            raise Exception()

    def to_string(self) -> str:
        return self.name


class CommandNode(Node):
    def __init__(self) -> None:
        self.node: Optional[Node] = None

    def parse(self, context: Context) -> None:
        if context.get_str_current_token() == "repeat":
            self.node = RepeatCommandNode()
            self.node.parse(context)
        else:
            self.node = PrimitiveCommandNode()
            self.node.parse(context)

    def to_string(self) -> str:
        return self.node.to_string() if self.node is not None else ""


class CommandListNode(Node):
    def __init__(self) -> None:
        self.list: list[CommandNode] = []

    def parse(self, context: Context) -> None:
        while (True):
            if context.current_token is None:
                raise Exception()
            elif context.get_str_current_token() == "end":
                context.skip_token("end")
                break
            else:
                node = CommandNode()
                node.parse(context)
                self.list.append(node)

    def to_string(self) -> str:
        string = "["
        for command in self.list:
            string = f"{string} {command.to_string()}"
        string = f"{string}]"
        return str(string)


class ProgramNode(Node):
    def parse(self, context: Context) -> None:
        context.skip_token("program")
        self.command_list_node = CommandListNode()
        self.command_list_node.parse(context)

    def to_string(self) -> str:
        return f"[program {self.command_list_node.to_string()}]"


if __name__ == '__main__':
    print("start:")
    # text = "program go go go end"
    text = "program repeat 4 repeat 3 go right go left end right end end"
    print(f"text: {text}")
    node = ProgramNode()
    node.parse(Context(text))
    print(f"node: {node.to_string()}")
    print(":end")
