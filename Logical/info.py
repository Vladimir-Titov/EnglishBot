from __future__ import annotations

from collections import deque
from typing import Dict

from environs import Env

from application import Level
from sheetsApi import SheetApi


class Info:
    env: Env = Env()
    __levels: Dict[str, Level] = dict()
    sheets_api: SheetApi = None
    task_queue: deque = deque()  # [Dict[str// level_name, List[str]// rus_answer] [{'B1': ['Поехали', 'Жаловаться']}, {'B2':[...]}]

    def __init__(self):
        self.sheets_api = SheetApi(self.env.str('credentials'), self.env.str('sheet_id'))
        self._set_levels()

    def __create_level(self, level: str) -> Level:
        level_dict: dict = self.env.dict(level)
        sheets_name: str = level_dict['sheets_name']
        level_name: str = level_dict['name']
        range_eng: str = level_dict['range_eng']
        range_rus: str = level_dict['range_rus']
        return Level(sheets_name, level_name, range_eng, range_rus, self.sheets_api)

    def _set_levels(self):
        self.sheets_api = SheetApi(self.env.str('credentials'), self.env.str('sheet_id'))
        for level in self.env.list('levels'):
            self.levels[level] = self.__create_level(level)

    @property
    def levels(self) -> Dict[str, Level]:
        return self.__levels
