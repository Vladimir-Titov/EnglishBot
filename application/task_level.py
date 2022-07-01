from sheetsApi import SheetApi


class Level:
    def __init__(self, name_sheet: str, level_name: str, sheet_range_eng: str, sheet_range_rus, sheet: SheetApi):
        self.name_sheet = name_sheet
        self.level_name = level_name
        self.sheet_range_eng = sheet_range_eng
        self.sheet_range_rus = sheet_range_rus
        self.dictionary = dict(zip(sheet.read_from_sheet(self.name_sheet, sheet_range_eng, 'COLUMNS'),
                                   sheet.read_from_sheet(self.name_sheet, sheet_range_rus, 'COLUMNS')))

    @property
    def dict(self):
        return self.dictionary

    @dict.setter
    def dict(self, dictionary):
        self.dictionary = dictionary
