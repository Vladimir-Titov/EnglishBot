from typing import Dict

from environs import Env

from application import Level
from sheetsApi import SheetApi
import random


class App:
    env = Env()
    env_message = Env()
    levels: Dict[str, Level] = dict()

    def __init__(self):
        self.sheets_api: SheetApi = None
        self.env_message.read_env('message.env')
        self.env.read_env('.env')

    def __set_setting(self):
        self.sheets_api = SheetApi(self.env.str('credentials'), self.env.str('sheet_id'))
        for level in self.env.list('levels'):
            self.levels[level] = self.__create_level(level)
            print(self.levels[level].dict)

    def __create_level(self, level: str) -> Level:
        level_dict: dict = self.env.dict(level)
        sheets_name: str = level_dict['sheets_name']
        level_name: str = level_dict['name']
        range_eng: str = level_dict['range_eng']
        range_rus: str = level_dict['range_rus']
        return Level(sheets_name, level_name, range_eng, range_rus, self.sheets_api)

    def run(self):
        self.__set_setting()
        print(self.levels)


if __name__ == '__main__':
    app = App()
    app.run()
