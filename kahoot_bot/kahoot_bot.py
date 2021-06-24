from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram import executor
from aiogram.types import (
    Message,
    CallbackQuery,
)
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import psycopg2
import random
import config
import buttons
from state import BotStates
from confs import answers, qwerty, links
import pathlib

PATH = pathlib.Path(__file__).parent


botst = BotStates()
storage = MemoryStorage()
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
pin = random.randrange(2001000, 3000000)

dbname = input("Your database name: ")
dbuser = input("Your database user: ")
dbpswd = input("Your database password: ")

conn = psycopg2.connect(
    dbname=dbname, user=dbuser, password=dbpswd, host="localhost"
)
cursor = conn.cursor()

nickname = []
user_id = []
nickname_points = {}


@dp.message_handler(commands=["start"])
async def start(message: Message):
    await botst.await_first.set()
    await message.answer(text="Введите pin-код для игры 🔒")


@dp.message_handler(commands=["play_game"])
async def game_pin(message: Message):
                                # Your TG id, type int.
                                #   |
    await bot.send_message(chat_id=, text=f"Game pin: {pin}")


@dp.message_handler(content_types=["text"], state=botst.await_first)
async def login(message: Message):
    str_pin = str(pin)
    if message.text == str_pin:
        await botst.await_second.set()
        await message.answer(
            text="Ну погнали ⏩ \nВведите свой никнейм: \nНик может иметь от 4 до 10 символов"
        )
    else:
        await message.answer(text="Если не знаешь pin-код игры, то узнай ☝🏼")


@dp.message_handler(content_types=["text"], state=botst.await_second)
async def nick(message: Message):
    if message.text:
        if len(message.text) > 3 and len(message.text) < 11:
            await message.answer(text="Принимается ")
            user_id.append(message.chat.id)
            nickname.append(message.text)
            nickname_points.update({message.from_user.id: 0})
            await message.answer(
                text="Готов(а)? ", reply_markup=buttons.Ready().readys()
            )
        else:
            await message.answer(text="Правила читай!")
    else:
        await message.text(text="Ты чего то не понял?")


@dp.callback_query_handler(state=botst.await_second)
async def call(call: CallbackQuery):
    if call.data == "1":
        await bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None,
        )
        await bot.send_message(chat_id=call.message.chat.id, text="Ждем создателя 👤")
        await botst.await_third.set()
    elif call.data == "0":
        await bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None,
        )
        await asyncio.sleep(5)
        await bot.send_message(
            chat_id=call.message.chat.id,
            text="А теперь? ",
            reply_markup=buttons.Ready().readys(),
        )


# ---------------------------------------------------------------------------------------------------
count1 = 0

                    # Random commands.
                            #   |
@dp.message_handler(commands=["list"], state=botst.await_third)
async def questions1(message: Message):
    global count1
    lis1 = []
    second1 = 20
    knopki = []

    for i in range(5):# Instead of 5, you can set a maximum limit of 25
        for id_users in user_id:
            await bot.send_photo(chat_id=id_users, photo=open(f"{PATH}{links[i]}", "rb"))
            knopok = await bot.send_message(
                chat_id=id_users,
                text=f"{qwerty[i]} \n{answers[i].get('condition')}",
                reply_markup=buttons.Quest().generate_buttons(
                    answers[i].get("solution")
                ),
            )
            knopki.append(knopok)
            timer_start_message = await bot.send_message(
                chat_id=id_users, text="У тебя 20 секунд на ответ . . . "
            )
            lis1.append(timer_start_message)
        for time in range(second1 - 1, 0, -1):
            for i in range(len(lis1)):
                count1 += 1
                await bot.edit_message_text(
                    chat_id=user_id[0], message_id=lis1[i].message_id, text=f"{time}"
                )
            await asyncio.sleep(0.5)
        try:
            for i in range(len(user_id)):
                await bot.edit_message_reply_markup(
                    chat_id=user_id[i], message_id=knopki[i].message_id, reply_markup=None
                )
        except:
            pass

@dp.callback_query_handler(state=botst.await_third)
async def call(call: CallbackQuery, state):
    if call.data == "True":
        await bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None,
        )
        await bot.send_message(chat_id=call.message.chat.id, text="Правильно ✅")
        point = 800 * (1+(1/count1))
        current_points = nickname_points.get(call.message.chat.id) + int(point)
        nickname_points.update({call.message.chat.id: current_points})
        nickname_points.update({call.message.chat.id: current_points})
    elif call.data == "False":
        await bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None,
        )
        await bot.send_message(chat_id=call.message.chat.id, text="Ты проиграл ❌")
    user_point = []
    for useid in user_id:
        ind = user_id.index(useid)
        user_point.append(nickname[ind])
        poi = nickname_points.get(useid)
        user_point.append(poi)
    await bot.send_message(chat_id=call.message.chat.id, text=str(user_point).replace('[', '').replace(']', '').replace(',', ':').replace("'", ''))

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)
