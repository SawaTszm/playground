import abc


class Banner:
    """元々提供されているクラス"""
    def __init__(self, text) -> None:
        self.text = text

    def show_with_paren(self) -> None:
        print(f"({self.text})")

    def show_with_aster(self) -> None:
        print(f"*{self.text}*")


class Print(metaclass=abc.ABCMeta):
    """今回の実装で必要とされている基底クラス"""
    @abc.abstractmethod
    def print_weak(self) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def print_strong(self) -> None:
        raise NotImplementedError()


class PrintBanner(Banner, Print):
    """元々提供されているものと必要とされているインターフェースを継承したAdapter"""
    def __init__(self, text) -> None:
        super().__init__(text)

    def print_weak(self) -> None:
        return self.show_with_paren()

    def print_strong(self) -> None:
        return self.show_with_aster()


class DelegationPrintBanner(Print):
    """委譲(delegation)を使うタイプのAdapter"""
    def __init__(self, banner: Banner) -> None:
        self.banner = banner

    def print_weak(self) -> None:
        return self.banner.show_with_paren()

    def print_strong(self) -> None:
        return self.banner.show_with_aster()


if __name__ == '__main__':
    print("start:")
    p = PrintBanner("hoge")
    p.print_weak()
    p.print_strong()
    dp = DelegationPrintBanner(Banner("huga"))
    dp.print_weak()
    dp.print_strong()
    print(":end")
