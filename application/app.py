from __future__ import annotations

from asyncio import sleep
from typing import Dict

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery

from application import MyEnv, TaskFromLevel, Task
from tel_bot import KeyboardGen


class App:
    bot: Bot = Bot(MyEnv.env.str('BOT_TOKEN'))
    dp: Dispatcher = Dispatcher(bot)

    def run(self):
        executor.start_polling(self.dp, skip_updates=True)

    @staticmethod
    @dp.message_handler(commands=['start', 'help'])
    async def hello_message(message: types.Message):
        from Logical import Info
        levels = Info().levels
        await message.reply(MyEnv.env_message.str('HELLO_MESSAGE'), reply=False)
        await sleep(1)
        await message.reply(MyEnv.env_message.str('CHOOSE_LEVEL'), reply=False,
                            reply_markup=KeyboardGen.get_level_kb(levels))

    @staticmethod
    @dp.callback_query_handler(KeyboardGen.level_cb.filter(level=MyEnv.env.list('levels')))
    async def choose_level(query: CallbackQuery, callback_data: Dict[str, str]):
        from Logical import Info
        task: Task = TaskFromLevel(Info().levels[callback_data['level']]).create_task()
        await query.message.reply(task.question, reply=False,
                                  reply_markup=KeyboardGen.get_task_kb(task.other,
                                                                       callback_data['level'],
                                                                       question=task.question))

    @staticmethod
    async def check_respond(data: str) -> bool:
        from Logical import Info
        data_lst: list = data.split('|')
        level_dict: dict = Info().levels[data_lst[0]].dict
        if level_dict[data_lst[1]] == data_lst[2]:
            return True
        return False

    @staticmethod
    @dp.callback_query_handler(KeyboardGen.respond_cb.filter())
    async def next_task(query: CallbackQuery, callback_data: Dict[str, str]):
        data_lst: list = callback_data['data'].split('|')
        if await App.check_respond(callback_data['data']):
            from Logical import Info
            task: Task = TaskFromLevel(Info().levels[data_lst[0]]).create_task()
            await query.answer('Right')
            await query.message.reply(task.question, reply=False,
                                      reply_markup=KeyboardGen.get_task_kb(task.other,
                                                                           data_lst[0],
                                                                           question=task.question))
        else:
            await query.answer('Wrong')
            await query.message.reply('Попробуй еще раз ответить', reply=False)


if __name__ == '__main__':
    app = App()
    app.run()
