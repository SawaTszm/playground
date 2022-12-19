import abc
from typing import Any


class Mediator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_colleagues(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def colleague_changed(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError()


class LoginMediator(Mediator):
    def __init__(self):
        self.authentication = False

    def create_colleagues(
        self, input_id: "ColleagueTextField", input_pw: "ColleagueTextField", button: "ColleagueButton"
    ):
        self.input_id = input_id
        self.input_pw = input_pw
        self.button = button

    def colleague_changed(self, component: "Colleague"):
        if component.name == "ID" or component.name == "PW":
            self.change_active_button()
        elif component.name == "Login Button":
            self.auth()

    def change_active_button(self):
        if (self.input_id.text and self.input_pw.text):
            print("ログインボタンがアクティブになりました")
            self.button.set_colleague_enabled(True)

    def auth(self):
        if self.input_id.text == "hoge" and self.input_pw.text == "huga":
            print("ログインしました")
            self.authentication = True
            self.input_id.text = ""
            self.input_pw.text = ""
            self.button.set_colleague_enabled(False)
        else:
            print("IDかパスワードが間違っています……")


class Colleague(metaclass=abc.ABCMeta):
    def __init__(self, mediator: Mediator, name: str, *args: Any, **kwargs: Any) -> None:
        self.mediator = mediator
        self.name = name

    @abc.abstractmethod
    def set_mediator(self, mediator: Mediator) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def set_colleague_enabled(self, enabled: bool) -> None:
        raise NotImplementedError()


class ColleagueButton(Colleague):
    def __init__(self, mediator: Mediator, name: str, caption: str = "") -> None:
        super().__init__(mediator, name)
        self.caption = caption
        self.is_active = False

    def set_mediator(self, mediator: Mediator) -> None:
        self.mediator = mediator

    def set_colleague_enabled(self, enabled: bool) -> None:
        self.is_active = enabled

    def click_button(self) -> None:
        if self.is_active:
            self.mediator.colleague_changed(self)
        else:
            print("ボタンは押せませんよ")


class ColleagueTextField(Colleague):
    def __init__(self, mediator: Mediator, name: str, text: str = "") -> None:
        super().__init__(mediator, name)
        self.text = text
        self.is_active = True

    def set_mediator(self, mediator: Mediator) -> None:
        self.mediator = mediator

    def set_colleague_enabled(self, enabled: bool) -> None:
        self.is_active = enabled

    def change_text(self, text: str) -> None:
        if self.is_active:
            self.text = text
            self.mediator.colleague_changed(self)
        else:
            print("このフォームはアクティブじゃありませんよ")


# 割愛: ColleagueCheckBoxクラス


if __name__ == "__main__":
    print("start:")
    print("成功:")
    userid, password = ["hoge", "huga"]
    mediator = LoginMediator()
    input_id = ColleagueTextField(mediator, "ID")
    input_pw = ColleagueTextField(mediator, "PW")
    button = ColleagueButton(mediator, "Login Button")
    mediator.create_colleagues(input_id, input_pw, button)

    input_id.change_text(userid)
    input_pw.change_text(password)
    button.click_button()

    print("失敗:")
    button.click_button()

    input_id.change_text(userid)
    input_pw.change_text("invaild password")
    button.click_button()
    print(":end")
