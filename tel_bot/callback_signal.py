from typing import Optional
from application import Task


class CallbackSignal:
    __signal: int = 0

    def __new__(cls, *args, **kwargs):
        cls.__signal += 1
        return super().__new__(cls)

    def __init__(self, action: str, text: str = '',task: Optional[Task] = None) -> None:
        self.__text = text
        self.__id = self.__signal
        self.__action = action
        self.__task = task

    @property
    def id(self) -> int:
        return self.__id

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str) -> None:
        self.__text = text

    @property
    def action(self) -> None:
        return self.__action

    @property
    def task(self) -> Optional[Task]:
        return self.__task


if __name__ == '__main__':
    a, b, c = CallbackSignal('hello', 'level'), CallbackSignal('one more', 'level'), CallbackSignal('more more more',
                                                                                                    'level')

    print([a.id, b.id, c.id])
