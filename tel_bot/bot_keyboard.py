from typing import Iterator, List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from application import MyEnv, TaskFromLevel, Task, Level
from callback_signal import CallbackSignal


class MyKeyboard:
    posts_cb = CallbackData('posts', 'id', 'action')
    next_cb = CallbackData('posts', 'id', 'action', 'answer')

    @staticmethod
    def create_level_keyboard() -> InlineKeyboardMarkup:
        markup: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=len(MyEnv.env.list('levels')))
        callbacks: List[CallbackSignal] = [CallbackSignal('create_level', text) for text in MyEnv.env.list('levels')]
        for elem in callbacks:
            markup.add(
                InlineKeyboardButton(elem.text, callback_data=MyKeyboard.posts_cb.new(id=elem.id, action=elem.action)))
        return markup

