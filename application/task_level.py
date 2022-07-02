from typing import Dict, List

from sheetsApi import SheetApi
import random


class Task:
    def __init__(self, question: str, answer: str, other: List[str]):
        self.__question = question
        self.__answer = answer
        self.__other = other

    @property
    def question(self) -> str:
        return self.__question

    @property
    def answer(self) -> str:
        return self.__answer

    @property
    def other(self) -> List[str]:
        return self.__other


class Level:
    def __init__(self, name_sheet: str, level_name: str, sheet_range_eng: str, sheet_range_rus,
                 sheet: SheetApi) -> None:
        self.name_sheet = name_sheet
        self.level_name = level_name
        self.sheet_range_eng = sheet_range_eng
        self.sheet_range_rus = sheet_range_rus
        self.dictionary = dict(zip(sheet.read_from_sheet(self.name_sheet, sheet_range_eng, 'COLUMNS'),
                                   sheet.read_from_sheet(self.name_sheet, sheet_range_rus, 'COLUMNS')))

    @property
    def dict(self) -> Dict[str, str]:
        return self.dictionary

    @dict.setter
    def dict(self, dictionary) -> None:
        self.dictionary = dictionary


class TaskFromLevel:
    def __init__(self, level: Level) -> None:
        self.__level: Level = level

    @property
    def level(self) -> Level:
        return self.__level

    def create_task(self) -> Task:
        level_copy = self.level.dict.copy()
        question: str = random.choice(list(self.level.dict.keys()))
        answer: str = self.level.dict[question]
        other: List[str] = list
        level_copy.pop(question)
        for i in range(3):
            other.append(random.choice(list(self.level.dict.values())))
        return Task(question, answer, other)
