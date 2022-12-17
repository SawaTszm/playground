
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        # TIL: __new__()が__init__()の前に呼ばれる。
        # 戻り値によっては__init__()は呼ばれない。
        if not hasattr(cls, "__instance__"):
            # インスタンスが生成されていない最初の一回だけ生成する
            # super(type(self), self)的な……？
            cls.__instance__ = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance__


if __name__ == '__main__':
    print("start:")
    obj1 = Singleton()
    obj2 = Singleton()
    if obj1 == obj2:
        print("同じインスタンスです")
    else:
        print("同じインスタンスじゃありません")
    print(":end")
