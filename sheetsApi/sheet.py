from pprint import pprint
from typing import List

import apiclient.discovery
import httplib2
from oauth2client.service_account import ServiceAccountCredentials


class SheetApi:

    def __init__(self, json_key: str, sheet_id: str):
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            json_key,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])
        self.httpAuth = self.credentials.authorize(httplib2.Http())
        self.service = apiclient.discovery.build('sheets', 'v4', http=self.httpAuth)
        self.sheetId = sheet_id

    def read_from_sheet(self, sheet_page: str, range_read: str, dimension: str) -> List[str]:
        values_d = self.service.spreadsheets().values().get(
            spreadsheetId=self.sheetId,
            range=(sheet_page + range_read),
            majorDimension=dimension
        ).execute()
        return values_d['values'][0]


if __name__ == '__main__':
    sheet = SheetApi('creds.json', '11YGMd2MpYSH6rxsjqKBgZ0qdyn7eHyGFJyY9GwIrm2U')
    values = sheet.read_from_sheet('Phrasal verbs B2!', 'C4:C', 'COLUMNS')
    pprint(values)
