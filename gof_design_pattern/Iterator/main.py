import abc
import typing


class IteratorInterface(metaclass=abc.ABCMeta):
    """Iteratorの機能を宣言するインターフェース"""

    @abc.abstractmethod
    def has_next(self) -> bool:
        raise NotImplementedError()

    @abc.abstractmethod
    def next(self) -> object:
        raise NotImplementedError()


class AggreegateInterface(metaclass=abc.ABCMeta):
    """IterableなObjectのインターフェース"""

    @abc.abstractmethod
    def iterator(self) -> IteratorInterface:
        raise NotImplementedError()


class Book:
    def __init__(self, name) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name


class BookShelfIterator(IteratorInterface):
    def __init__(self, bookshelf) -> None:
        self.__bookshelf = bookshelf
        self.__index = 0

    def has_next(self) -> bool:
        if self.__index < self.__bookshelf.get_length():
            return True
        return False

    def next(self) -> Book:
        book = self.__bookshelf.get_book_at(self.__index)
        self.__index += 1
        return book


class BookShelf(AggreegateInterface):
    def __init__(self, maxsize: int) -> None:
        self.__books: typing.List[Book] = []
        self.__last: int = 0
        self.__maxsize = maxsize

    def get_book_at(self, index: int) -> Book:
        return self.__books[index]

    def append_book(self, book: Book) -> None:
        if self.__last >= self.__maxsize:
            raise Exception

        self.__books.append(book)
        self.__last += 1

    def get_length(self) -> int:
        return self.__last

    def change_maxsize(self, maxsize: int) -> None:
        if self.__last > maxsize:
            raise Exception
        self.__maxsize = maxsize

    def iterator(self) -> BookShelfIterator:
        return BookShelfIterator(self)


if __name__ == '__main__':
    print("start:")
    bookshelf = BookShelf(3)
    bookshelf.append_book(Book("first book"))
    bookshelf.append_book(Book("second book"))
    bookshelf.append_book(Book("third book"))
    bookshelf.change_maxsize(5)
    bookshelf.append_book(Book("fourth book"))
    bookshelf.append_book(Book("fifth book"))

    iterator = bookshelf.iterator()
    print("search books:")
    while (iterator.has_next()):
        book = iterator.next()
        print(f"  * {book.get_name()}")
    print(":end")
