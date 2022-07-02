from typing import Dict

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.callback_data import CallbackData

from application import MyEnv
from bot_keyboard import MyKeyboard
from asyncio import sleep


class MyBot:
    bot: Bot = Bot(MyEnv.env.str('BOT_TOKEN'))
    dp: Dispatcher = Dispatcher(bot)
    keyboard_level: InlineKeyboardMarkup = MyKeyboard.create_level_keyboard()

    @staticmethod
    @dp.message_handler(commands=['start', 'help'])
    async def hello_message(message: types.Message):
        await message.reply(MyEnv.env_message.str('HELLO_MESSAGE'), reply=False)
        await sleep(1)
        await message.reply(MyEnv.env_message.str('CHOOSE_LEVEL'), reply=False, reply_markup=MyBot.keyboard_level)


if __name__ == '__main__':
    bot = MyBot()
    executor.start_polling(bot.dp, skip_updates=True)
