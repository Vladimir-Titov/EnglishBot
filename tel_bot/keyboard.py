from typing import Dict, List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from application import Level


class KeyboardGen:
    level_cb: CallbackData = CallbackData('start', 'level')
    respond_cb: CallbackData = CallbackData('start', 'data')

    @staticmethod
    def get_level_kb(levels: Dict[str, Level]) -> InlineKeyboardMarkup:
        keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=2)
        for level in levels:
            keyboard.row(InlineKeyboardButton(level, callback_data=KeyboardGen.level_cb.new(level=level)))
        return keyboard

    @staticmethod
    def get_task_kb(responds: List[str], level: str, question: str):
        keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=2)
        for respond in responds:
            data: list = [level, question, respond]
            # enc_data = '|'.join(data).encode()
            # print(enc_data)
            data = '|'.join(data)
            keyboard.row(InlineKeyboardButton(respond, callback_data=KeyboardGen.respond_cb.new(data=data)))
        return keyboard


if __name__ == '__main__':
    import base64
    from sys import getsizeof

    message = "B2|Hello|Приветdasdasdasd"
    print(getsizeof(message.encode()))
    # message_bytes = message.encode('utf-8')
    # base64_bytes = base64.b64encode(message_bytes)
    # base64_message = base64_bytes.decode('utf-8')
    # print(base64_message)
    # base64_bytes = base64_message.encode('utf-8')
    # message_bytes = base64.b64decode(base64_bytes)
    # message = message_bytes.decode('utf-8')
    # print(message)
