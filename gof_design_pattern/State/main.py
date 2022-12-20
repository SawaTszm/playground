import abc
from pprint import pprint


class Context(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set_clock(self, hour: int) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def change_state(self, state: "State") -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def call_security_center(self, msg: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def record_log(self, msg: str) -> None:
        raise NotImplementedError()


class State(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do_clock(self, context: Context, hour: int) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def do_use(self, context: Context) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def do_alarm(self, context: Context) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def do_phone(self, context: Context) -> None:
        raise NotImplementedError()


class DayState(State):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "__instance__"):
            cls.__instance__ = super(DayState, cls).__new__(cls, *args, **kwargs)
        return cls.__instance__

    def do_clock(self, context: Context, hour: int) -> None:
        if hour < 9 or 17 <= hour:
            context.change_state(NightState())

    def do_use(self, context: Context) -> None:
        context.record_log("金庫使用(昼間)")

    def do_alarm(self, context: Context) -> None:
        context.call_security_center("非常ベル(昼間)")

    def do_phone(self, context: Context) -> None:
        context.call_security_center("通常の通話(昼間)")

    def to_string(self) -> str:
        return "[昼間]"


class NightState(State):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "__instance__"):
            cls.__instance__ = super(NightState, cls).__new__(cls, *args, **kwargs)
        return cls.__instance__

    def do_clock(self, context: Context, hour: int) -> None:
        if 9 <= hour or hour < 17:
            context.change_state(DayState())

    def do_use(self, context: Context) -> None:
        context.call_security_center("非常: 夜間の金庫使用")

    def do_alarm(self, context: Context) -> None:
        context.call_security_center("非常ベル(夜間)")

    def do_phone(self, context: Context) -> None:
        context.record_log("夜間の通話録音")

    def to_string(self) -> str:
        return "[夜間]"


class SafeContext(Context):
    def __init__(self) -> None:
        self.hour = 0
        self.state = NightState()
        self.log: list[str] = []

    def set_clock(self, hour: int) -> None:
        self.hour = hour
        self.state.do_clock(self, hour)

    def use_button(self) -> None:
        # 金庫を使う
        self.state.do_use(self)

    def use_alarm_buttom(self) -> None:
        # 非常用ベルを使う
        self.state.do_alarm(self)

    def call(self) -> None:
        # 通常通話
        self.state.do_phone(self)

    def change_state(self, state: State) -> None:
        print(f"{self.state.to_string()}から{state.to_string()}に変わりました")
        self.state = state

    def call_security_center(self, msg: str) -> None:
        self.log.append(f"call! {msg}")

    def record_log(self, msg: str) -> None:
        self.log.append(f"record ... {msg}")


if __name__ == '__main__':
    print("start:")
    sc = SafeContext()
    
    sc.use_button()  # 夜間の金庫使用
    sc.call()  # 夜間の通話
    sc.use_alarm_buttom()  # 夜間の非常ボタン使用

    sc.set_clock(10)  # 昼間
    sc.use_button()  # 昼間の金庫使用
    sc.call()  # 昼間の通話
    sc.use_alarm_buttom()  # 昼間の非常ボタン使用

    print("ログ一覧: ")
    pprint(sc.log)
    print(":end")
