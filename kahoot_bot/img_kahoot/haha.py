# Основа
from typing import Text
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram import executor
from aiogram.types import Message, ParseMode, document, mask_position, message, CallbackQuery, user
from aiogram.dispatcher.filters import state
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# Второстепенные
import asyncio
import csv
import psycopg2
import random
import requests
import config
import pathlib
import time
import buttons
from state import BotStates

botst = BotStates()
storage = MemoryStorage()

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

PATH = pathlib.Path(__file__).parent
pin = random.randrange(2001000, 3000000)

nickname = ''
user_id = []
nickname_points = {}

first = 0.14
second = 0.06
third = 0.02
four = -0.02
five = -0.06

@dp.message_handler(commands=['start'])
async def start(message: Message):
    await botst.await_first.set()
    await message.answer(text='Введите pin-код для игры 🔒')

@dp.message_handler(commands=['play_game'])
async def game_pin(message: Message):
    await bot.send_message(chat_id=1624089338, text=f'Game pin: {pin}')
   
@dp.message_handler(content_types=['text'], state=botst.await_first)
async def login(message: Message):
    str_pin = str(pin)
    if message.text == str_pin:
        await botst.await_second.set()
        await message.answer(text='Ну погнали ⏩ \nВведите свой никнейм: \nНик может иметь от 4 до 10 символов')
    else:
        await message.answer(text='Если не знаешь pin-код игры, то узнай ☝🏼')

@dp.message_handler(content_types=['text'], state=botst.await_second)
async def nick(message: Message, state):
    if message.text:
        if len(message.text) > 3 and len(message.text) < 11:
            await botst.await_third.set()
            await message.answer(text='Принимается ')
            user_id.append(message.chat.id)
            nickname = message.text
            nickname_points.update({message.text: 0})
            await message.answer(text='Готов(а)? ', reply_markup=buttons.Ready().readys())
            await botst.await_third.set()
        else:
            await message.answer(text='Правила читай!')
    else:
        await message.text(text='Ты чего то не понял?')


@dp.message_handler(content_types=['text'], state=botst.await_third)
async def nachalo(message: Message, state):
    if message.text:
        if message.text == 'Готов ✅':
            
        elif message.text == 'Не готов ❌':
            await asyncio.sleep(5)
            await message.answer(text='А теперь? ', reply_markup=buttons.Ready().readys())
    else:
        await message.text(text='Ты чего то не понял?')





@dp.message_handler(state=botst.await_four)
async def questions(message: Message):
    for user in user_id:
        await bot.send_photo(chat_id=user, photo=open('/home/asus/Desktop/kahoot_bot/img_kahoot.py/1img.webp', 'rb'))
        await bot.send_message(chat_id=user, text='Что выведет данная команда?\n🟥 3 + 2\n🟦 (5)\n🟨 5\n🟩 SyntaxError', reply_markup=buttons.Quest().quest1())
        timer_start_message = await message.answer(text='У тебя 20 секунд на ответ . . . ')
        for time in range(10, 0, -1):
            await asyncio.sleep(1)
            await bot.edit_message_text(chat_id=user, message_id=timer_start_message.message_id, text=f'{time}')

@dp.callback_query_handler(state=botst.await_third)
async def call(call: CallbackQuery):
    if call.data == '5':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
        for i in range(1):
            nickname_points.update({str(nickname): first})
        await bot.send_message(chat_id=call.message.chat.id, text=nickname_points)
        await botst.await_four.set()
    elif call.data == '(5)' or call.data == '3 + 2' or call.data == 'SyntaxError':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
        await botst.await_four.set()

#---------------------------------------------------------------------------------------------------

@dp.message_handler(state=botst.await_four)
async def questions(message: Message):
    for i in range(len(user_id)):
        await bot.send_photo(chat_id=message.chat.id, photo=open('/home/asus/Desktop/kahoot_bot/img_kahoot.py/2img.webp', 'rb'))
        await bot.send_message(chat_id=message.chat.id, text='Python это змея?\n🟥 False\n🟦 True', reply_markup=buttons.Quest().quest2())
        timer_start_message = await message.answer(text='У тебя 10 секунд на ответ . . . ')
    for time in range(10, 0, -1):
        await asyncio.sleep(1)
        await bot.edit_message_text(chat_id=message.chat.id, message_id=timer_start_message.message_id, text=f'{time}')


@dp.callback_query_handler(state=botst.await_four)
async def call(call: CallbackQuery):
    if call.data == 'False':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
        await botst.await_five.set()
    elif call.data == 'True':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
        await botst.await_five.set()

#---------------------------------------------------------------------------------------------------

@dp.message_handler(state=botst.await_five)
async def questions(message: Message):
    for i in range(len(user_id)):
        await bot.send_photo(chat_id=message.chat.id, photo=open('/home/asus/Desktop/kahoot_bot/img_kahoot.py/3img.webp', 'rb'))
        await bot.send_message(chat_id=message.chat.id, text='Какого знака не может быть в переменной?\n🟥 -\n🟦 Цифры\n🟨 _\n🟩 Буквы', reply_markup=buttons.Quest().quest3())
        timer_start_message = await message.answer(text='У тебя 20 секунд на ответ . . . ')
    for time in range(20, 0, -1):
        await asyncio.sleep(1)
        await bot.edit_message_text(chat_id=message.chat.id, message_id=timer_start_message.message_id, text=f'{time}')

@dp.callback_query_handler(state=botst.await_five)
async def call(call: CallbackQuery):
    if call.data == '-':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
        await botst.await_six.set()
    elif call.data == 'num' or call.data == 'tamga' or call.data == '_':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
        await botst.await_six.set()

#---------------------------------------------------------------------------------------------------

@dp.message_handler(state=botst.await_six)
async def questions(message: Message):
    for i in range(len(user_id)):
        await bot.send_photo(chat_id=message.chat.id, photo=open('/home/asus/Desktop/kahoot_bot/img_kahoot.py/4img.webp', 'rb'))
        await bot.send_message(chat_id=message.chat.id, text='Что выведет данная команда?\n🟥 1\n🟦 a\n🟨 b\n🟩 Error', reply_markup=buttons.Quest().quest4())
        timer_start_message = await message.answer(text='У тебя 20 секунд на ответ . . . ')
    for time in range(20, 0, -1):
        await asyncio.sleep(1)
        await bot.edit_message_text(chat_id=message.chat.id, message_id=timer_start_message.message_id, text=f'{time}')

@dp.callback_query_handler(state=botst.await_six)
async def call(call: CallbackQuery):
    if call.data == 'Error':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
        await botst.await_seven.set()
    elif call.data == 'a' or call.data == 'b' or call.data == '1':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
        await botst.await_seven.set()

#---------------------------------------------------------------------------------------------------

@dp.message_handler(state=botst.await_seven)
async def questions(message: Message):
    for i in range(len(user_id)):
        await bot.send_photo(chat_id=message.chat.id, photo=open('/home/asus/Desktop/kahoot_bot/img_kahoot.py/5img.webp', 'rb'))
        await bot.send_message(chat_id=message.chat.id, text='Какие цвета на лого python?\n🟥 Фиолетовый-Черный\n🟦 Синий-Зеленый\n🟨 Явно змея\n🟩 Желтый-Синий', reply_markup=buttons.Quest().quest5())
        timer_start_message = await message.answer(text='У тебя 20 секунд на ответ . . . ')
    for time in range(20, 0, -1):
        await asyncio.sleep(1)
        await bot.edit_message_text(chat_id=message.chat.id, message_id=timer_start_message.message_id, text=f'{time}')

@dp.callback_query_handler(state=botst.await_seven)
async def call(call: CallbackQuery):
    if call.data == 'True':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
        await botst.await_eight.set()
    elif call.data == 'False':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
        await botst.await_eight.set()

#---------------------------------------------------------------------------------------------------

@dp.message_handler(state=botst.await_eight)
async def questions(message: Message):
    for i in range(len(user_id)):
        await bot.send_photo(chat_id=message.chat.id, photo=open('/home/asus/Desktop/kahoot_bot/img_kahoot.py/6img.webp', 'rb'))
        await bot.send_message(chat_id=message.chat.id, text='Что выведет данная команда?\n🟥 От 1 до 100\n🟦 i 100 раз\n🟨 Error\n🟩 От 0 до 99', reply_markup=buttons.Quest().quest6())
        timer_start_message = await message.answer(text='У тебя 20 секунд на ответ . . . ')
    for time in range(20, 0, -1):
        await asyncio.sleep(1)
        await bot.edit_message_text(chat_id=message.chat.id, message_id=timer_start_message.message_id, text=f'{time}')

@dp.callback_query_handler(state=botst.await_eight)
async def call(call: CallbackQuery):
    if call.data == 'prav':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
        await botst.await_nine.set()
    elif call.data == 'false6':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
        await botst.await_nine.set()

#---------------------------------------------------------------------------------------------------

@dp.message_handler(state=botst.await_nine)
async def questions(message: Message):
    for i in range(len(user_id)):
        await bot.send_photo(chat_id=message.chat.id, photo=open('/home/asus/Desktop/kahoot_bot/img_kahoot.py/7img.webp', 'rb'))
        await bot.send_message(chat_id=message.chat.id, text='Сколько видов импорта сущуствует?\n🟥 4\n🟦 1\n🟨 2\n🟩 3', reply_markup=buttons.Quest().quest7())
        timer_start_message = await message.answer(text='У тебя 20 секунд на ответ . . . ')
    for time in range(20, 0, -1):
        await asyncio.sleep(1)
        await bot.edit_message_text(chat_id=message.chat.id, message_id=timer_start_message.message_id, text=f'{time}')

@dp.callback_query_handler(state=botst.await_nine)
async def call(call: CallbackQuery, state):
    if call.data == 'True':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
        state.finish()
    elif call.data == 'False':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
        state.finish()







if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)
