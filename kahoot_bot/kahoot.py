# Основа
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram import executor
from aiogram.types import Message, ParseMode, document, mask_position, message, CallbackQuery, user, ReplyKeyboardRemove
from aiogram.dispatcher.filters import state
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# Второстепенные
import asyncio
import psycopg2
import random
import config
import pathlib
import buttons
from state import BotStates

botst = BotStates()
storage = MemoryStorage()

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

PATH = pathlib.Path(__file__).parent
pin = random.randrange(2001000, 3000000)

nickname = []
user_id = []
nickname_points = {}

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
            await message.answer(text='Принимается ')
            user_id.append(message.chat.id)
            nickname.append(message.text)
            nickname_points.update({message.from_user.id: 0})
            await message.answer(text='Готов(а)? ', reply_markup=buttons.Ready().readys())
            await botst.await_zapas.set()
        else:
            await message.answer(text='Правила читай!')
    else:
        await message.text(text='Ты чего то не понял?')

@dp.callback_query_handler(state=botst.await_zapas)
async def call(call: CallbackQuery):
    if call.data == '1':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Ждем создателя 👤')
        await botst.await_third.set()
    elif call.data == '0':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await asyncio.sleep(5)
        await bot.send_message(chat_id=call.message.chat.id, text='А теперь? ', reply_markup=buttons.Ready().readys())
    else:
        await bot.send_message(chat_id=call.message.chat.id, text='Мда . . . ')

#---------------------------------------------------------------------------------------------------
# count1 = 0
# @dp.message_handler(commands=['list'], state=botst.await_third)
# async def questions1(message: Message):
#     global count1
#     lis1 = []
#     second1 = 20
#     knopki = []
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/1img.webp', 'rb'))
#         knopok = await bot.send_message(chat_id=id_users, text='Что выведет данная команда?\n🟥 3 + 2\n🟦 (5)\n🟨 5\n🟩 SyntaxError', reply_markup=buttons.Quest().quest1())
#         knopki.append(knopok)
#         timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
#         lis1.append(timer_start_message)
#     for time in range(second1-1, 0, -1):
#         for i in range(len(lis1)):
#             count1 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis1[i].message_id, text=f'{time}')
#         await asyncio.sleep(0.5)
#     for i in range(len(user_id)):
#         await bot.edit_message_reply_markup(chat_id=user_id[i], message_id=knopki[i].message_id, reply_markup=None)
#     await botst.await_four.set()

# @dp.callback_query_handler(state=botst.await_third)
# async def call(call: CallbackQuery):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count1))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#     await botst.await_four.set()

# #---------------------------------------------------------------------------------------------------
# count2 = 0
# @dp.message_handler(commands=['list'], state=botst.await_four)
# async def questions2(message: Message):
#     global count2
#     lis = []
#     second = 10
#     knopki = []
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/2img.webp', 'rb'))
#         knopok = await bot.send_message(chat_id=id_users, text='Python это змея?\n🟥 False\n🟦 True', reply_markup=buttons.Quest().quest2())
#         knopki.append(knopok)
#         timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 10 секунд на ответ . . . ')
#         lis.append(timer_start_message)
#     for time in range(second-1, 0, -1):
#         for i in range(len(lis)):
#             count2 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i].message_id, text=f'{time}')
#         await asyncio.sleep(0.5)
#     for i in range(len(user_id)):
#         await bot.edit_message_reply_markup(chat_id=user_id[i], message_id=knopki[i].message_id, reply_markup=None)
#     await botst.await_five.set()

# @dp.callback_query_handler(state=botst.await_four)
# async def call(call: CallbackQuery):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count2))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#     await botst.await_five.set()

# #---------------------------------------------------------------------------------------------------
# count3 = 0
# @dp.message_handler(commands=['list'], state=botst.await_five)
# async def questions3(message: Message):
#     global count3
#     lis = []
#     second = 20
#     knopki = []
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/3img.webp', 'rb'))
#         knopok = await bot.send_message(chat_id=id_users, text='Какого знака не может быть в переменной?\n🟥 -\n🟦 Цифры\n🟨 _\n🟩 Буквы', reply_markup=buttons.Quest().quest3())
#         knopki.append(knopok)
#         timer_start_message = await bot.send_message(chat_id=id_users , text='У тебя 20 секунд на ответ . . . ')
#         lis.append(timer_start_message)
#     for time in range(second-1, 0, -1):
#         for i in range(len(lis)):
#             count3 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i].message_id, text=f'{time}')
#         await asyncio.sleep(0.5)
#     for i in range(len(user_id)):
#         await bot.edit_message_reply_markup(chat_id=user_id[i], message_id=knopki[i].message_id, reply_markup=None)
#     await botst.await_six.set()

# @dp.callback_query_handler(state=botst.await_five)
# async def call(call: CallbackQuery):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count3))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#     await botst.await_six.set()

# #---------------------------------------------------------------------------------------------------
# count4 = 0
# @dp.message_handler(commands=['list'], state=botst.await_six)
# async def questions4(message: Message):
#     global count4
#     lis = []
#     second = 20
#     knopki = []
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/4img.webp', 'rb'))
#         knopok = await bot.send_message(chat_id=id_users, text='Что выведет данная команда?\n🟥 1\n🟦 a\n🟨 b\n🟩 Error', reply_markup=buttons.Quest().quest4())
#         knopki.append(knopok)
#         timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
#         lis.append(timer_start_message)
#     for time in range(second-1, 0, -1):
#         for i in range(len(lis)):
#             count4 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i].message_id, text=f'{time}')
#         await asyncio.sleep(0.5)
#     for i in range(len(user_id)):
#         await bot.edit_message_reply_markup(chat_id=user_id[i], message_id=knopki[i].message_id, reply_markup=None)
#     await botst.await_seven.set()

# @dp.callback_query_handler(state=botst.await_six)
# async def call(call: CallbackQuery):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count4))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#     await botst.await_seven.set()

# #---------------------------------------------------------------------------------------------------
# count5 = 0
# @dp.message_handler(commands=['list'], state=botst.await_seven)
# async def questions5(message: Message):
#     global count5
#     lis = []
#     second = 20
#     knopki = []
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/5img.webp', 'rb'))
#         knopok = await bot.send_message(chat_id=id_users, text='Какие цвета на лого python?\n🟥 Фиолетовый-Черный\n🟦 Синий-Зеленый\n🟨 Явно змея\n🟩 Желтый-Синий', reply_markup=buttons.Quest().quest5())
#         knopki.append(knopok)
#         timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
#         lis.append(timer_start_message)
#     for time in range(second-1, 0, -1):
#         for i in range(len(lis)):
#             count5 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i].message_id, text=f'{time}')
#         await asyncio.sleep(0.5)
#     for i in range(len(user_id)):
#         await bot.edit_message_reply_markup(chat_id=user_id[i], message_id=knopki[i].message_id, reply_markup=None)
#     state.finish()

# @dp.callback_query_handler(state=botst.await_seven)
# async def call(call: CallbackQuery, state):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count5))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#     user_point = []
#     for useid in user_id:
#         ind = user_id.index(useid)
#         user_point.append(nickname[ind])
#         poi = nickname_points.get(useid)
#         user_point.append(poi)
#     await bot.send_message(chat_id=call.message.chat.id, text=str(user_point).replace('[', '').replace(']', '').replace(',', ':').replace("'", ''))
#     state.finish()

# ---------------------------------------------------------------------------------------------------
count1 = 0
@dp.message_handler(commands=['list'], state=botst.await_third)
async def questions6(message: Message):
    global count1
    lis = []
    second = 20
    knopki = []
    for id_users in user_id:
        await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/6img.webp', 'rb'))
        knopok = await bot.send_message(chat_id=id_users, text='Что выведет данная команда?\n🟥 От 1 до 100\n🟦 i 100 раз\n🟨 Error\n🟩 От 0 до 99', reply_markup=buttons.Quest().quest6())
        knopki.append(knopok)
        timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
        lis.append(timer_start_message)
    for time in range(second-1, 0, -1):
        for i in range(len(lis)):
            count1 += 1
            await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i].message_id, text=f'{time}')
        await asyncio.sleep(0.5)
    for i in range(len(user_id)):
        await bot.edit_message_reply_markup(chat_id=user_id[i], message_id=knopki[i].message_id, reply_markup=None)
    await botst.await_four.set()


@dp.callback_query_handler(state=botst.await_third)
async def call(call: CallbackQuery):
    if call.data == 'True':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
        point = 800 * (1+(1/count1))
        current_points = nickname_points.get(call.message.chat.id) + int(point)
        nickname_points.update({call.message.chat.id: current_points})
    elif call.data == 'False':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
    await botst.await_four.set()

#---------------------------------------------------------------------------------------------------
count2 = 0
@dp.message_handler(commands=['list'], state=botst.await_four)
async def questions7(message: Message):
    global count2
    lis = []
    second = 20
    knopki = []
    for id_users in user_id:
        await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/7img.webp', 'rb'))
        knopok = await bot.send_message(chat_id=id_users, text='Что выведет данная команда?\n🟥 (abc)\n🟦 abc\n🟨 a+b+c\n🟩 Error', reply_markup=buttons.Quest().quest7())
        knopki.append(knopok)
        timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
        lis.append(timer_start_message)
    for time in range(second-1, 0, -1):
        for i in range(len(lis)):
            count2 += 1
            await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i].message_id, text=f'{time}')
        await asyncio.sleep(0.5)
    for i in range(len(user_id)):
        await bot.edit_message_reply_markup(chat_id=user_id[i], message_id=knopki[i].message_id, reply_markup=None)
    await botst.await_five.set()


@dp.callback_query_handler(state=botst.await_four)
async def call(call: CallbackQuery):
    if call.data == 'True':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
        point = 800 * (1+(1/count2))
        current_points = nickname_points.get(call.message.chat.id) + int(point)
        nickname_points.update({call.message.chat.id: current_points})
    elif call.data == 'False':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
    await botst.await_five.set()

#---------------------------------------------------------------------------------------------------
count3 = 0
@dp.message_handler(commands=['list'], state=botst.await_five)
async def questions7(message: Message):
    global count3
    lis = []
    second = 20
    knopki = []
    for id_users in user_id:
        await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/8img.webp', 'rb'))
        knopok = await bot.send_message(chat_id=id_users, text='Создатель python человек?\n🟥 True\n🟦 False', reply_markup=buttons.Quest().quest8())
        knopki.append(knopok)
        timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
        lis.append(timer_start_message)
    for time in range(second-1, 0, -1):
        for i in range(len(lis)):
            count3 += 1
            await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i].message_id, text=f'{time}')
        await asyncio.sleep(0.5)
    for i in range(len(user_id)):
        await bot.edit_message_reply_markup(chat_id=user_id[i], message_id=knopki[i].message_id, reply_markup=None)
    await botst.await_six.set()


@dp.callback_query_handler(state=botst.await_five)
async def call(call: CallbackQuery):
    if call.data == 'True':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
        point = 800 * (1+(1/count3))
        current_points = nickname_points.get(call.message.chat.id) + int(point)
        nickname_points.update({call.message.chat.id: current_points})
    elif call.data == 'False':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
    await botst.await_six.set()

#---------------------------------------------------------------------------------------------------
count4 = 0
@dp.message_handler(commands=['list'], state=botst.await_six)
async def questions7(message: Message):
    global count4
    lis = []
    second = 20
    knopki = []
    for id_users in user_id:
        await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/9img.webp', 'rb'))
        knopok = await bot.send_message(chat_id=id_users, text='Что выведет данная команда?\n🟥 TypeError\n🟦 274, 2\n🟨 274 + 2\n🟩 NameError', reply_markup=buttons.Quest().quest9())
        knopki.append(knopok)
        timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
        lis.append(timer_start_message)
    for time in range(second-1, 0, -1):
        for i in range(len(lis)):
            count4 += 1
            await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i].message_id, text=f'{time}')
        await asyncio.sleep(0.5)
    for i in range(len(user_id)):
        await bot.edit_message_reply_markup(chat_id=user_id[i], message_id=knopki[i].message_id, reply_markup=None)
    await botst.await_seven.set()


@dp.callback_query_handler(state=botst.await_six)
async def call(call: CallbackQuery):
    if call.data == 'True':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
        point = 800 * (1+(1/count4))
        current_points = nickname_points.get(call.message.chat.id) + int(point)
        nickname_points.update({call.message.chat.id: current_points})
    elif call.data == 'False':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
    await botst.await_seven.set()

#---------------------------------------------------------------------------------------------------
count5 = 0
@dp.message_handler(commands=['list'], state=botst.await_seven)
async def questions7(message: Message, state):
    global count5
    lis = []
    second = 20
    knopki = []
    for id_users in user_id:
        await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/10img.webp', 'rb'))
        knopok = await bot.send_message(chat_id=id_users, text='Что выведет данная команда?\n🟥 True\n🟦 False\n🟨 TypeError\n🟩 1', reply_markup=buttons.Quest().quest10())
        knopki.append(knopok)
        timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
        lis.append(timer_start_message)
    for time in range(second-1, 0, -1):
        for i in range(len(lis)):
            count5 += 1
            await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i].message_id, text=f'{time}')
        await asyncio.sleep(0.5)
    for i in range(len(user_id)):
        await bot.edit_message_reply_markup(chat_id=user_id[i], message_id=knopki[i].message_id, reply_markup=None)
    state.finish()

@dp.callback_query_handler(state=botst.await_seven)
async def call(call: CallbackQuery, state):
    if call.data == 'True':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
        point = 800 * (1+(1/count5))
        current_points = nickname_points.get(call.message.chat.id) + int(point)
        nickname_points.update({call.message.chat.id: current_points})
    elif call.data == 'False':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
    state.finish()

# # #---------------------------------------------------------------------------------------------------
# count1 = 0
# @dp.message_handler(commands=['list'], state=botst.await_third)
# async def questions6(message: Message):
#     global count1
#     lis = []
#     second = 20
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/11img.webp', 'rb'))
#         await bot.send_message(chat_id=id_users, text='Python - интерпретируемый язык или компилируемый?\n🟥 Интерпретируемый язык\n🟦 Компилируемый язык', reply_markup=buttons.Quest().quest11())
#         timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
#         lis.append(timer_start_message)
#     for time in range(second-1, 0, -1):
#         for i in range(len(lis)):
#             count1 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i].message_id, text=f'{time}')
#         await asyncio.sleep(0.5)


# @dp.callback_query_handler(state=botst.await_third)
# async def call(call: CallbackQuery):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count1))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
#         await botst.await_four.set()
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#         await botst.await_four.set()

# #---------------------------------------------------------------------------------------------------
# count2 = 0
# @dp.message_handler(commands=['list'], state=botst.await_four)
# async def questions7(message: Message):
#     global count2
#     lis = []
#     second = 20
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/12img.webp', 'rb'))
#         await bot.send_message(chat_id=id_users, text='Сколько видов импорта сущуствует?\n🟥 4\n🟦 1\n🟨 2\n🟩 3', reply_markup=buttons.Quest().quest12())
#         timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
#         lis.append(timer_start_message)
#     for time in range(second-1, 0, -1):
#         for i in range(len(lis)):
#             count3 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i].message_id, text=f'{time}')
#         await asyncio.sleep(0.5)


# @dp.callback_query_handler(state=botst.await_four)
# async def call(call: CallbackQuery):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count2))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
     
#         await botst.await_five.set()
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#         await botst.await_five.set()

# #---------------------------------------------------------------------------------------------------
# count3 = 0
# @dp.message_handler(commands=['list'], state=botst.await_five)
# async def questions7(message: Message):
#     global count3
#     lis = []
#     second = 20
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/13img.webp', 'rb'))
#         await bot.send_message(chat_id=id_users, text='Можно ли создать декоратор из класса?\n🟥 True\n🟦 False', reply_markup=buttons.Quest().quest13())
#         timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
#         lis.append(timer_start_message)
#     for time in range(second-1, 0, -1):
#         for i in range(len(lis)):
#             count3 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i]                                vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvtt


# @dp.callback_query_handler(state=botst.await_five)
# async def call(call: CallbackQuery):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count3))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
     
#         await botst.await_six.set()
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#         await botst.await_six.set()

# #---------------------------------------------------------------------------------------------------
# count4 = 0
# @dp.message_handler(commands=['list'], state=botst.await_six)
# async def questions7(message: Message):
#     global count4
#     lis = []
#     second = 20
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/14img.webp', 'rb'))
#         await bot.send_message(chat_id=id_users, text='Можно ли использовать несколько декораторов для одной функции?\n🟥 True\n🟦 False', reply_markup=buttons.Quest().quest14())
#         timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
#         lis.append(timer_start_message)
#     for time in range(second-1, 0, -1):
#         for i in range(len(lis)):
#             count4 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i


# @dp.callback_query_handler(state=botst.await_six)
# async def call(call: CallbackQuery):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count4))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
     
#         await botst.await_seven.set()
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#         await botst.await_seven.set()

# #---------------------------------------------------------------------------------------------------
# count5 = 0
# @dp.message_handler(commands=['list'], state=botst.await_seven)
# async def questions7(message: Message):
#     global count5
#     lis = []
#     second = 20
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/15img.webp', 'rb'))
#         await bot.send_message(chat_id=id_users, text='Как пишутся комментарии в питоне?\n🟥 @\n🟦 #\n🟨 *\n🟩 +', reply_markup=buttons.Quest().quest15())
#         timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
#         lis.append(timer_start_message)
#     for time in range(second-1, 0, -1):
#         for i in range(len(lis)):
#             count5 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i
# for konina in user_id:]    .message_id, text=f'{time}')


# @dp.callback_query_handler(state=botst.await_seven)
# async def call(call: CallbackQuery, state):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count5))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
     
#         state.finish()
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#         state.finish()

# #---------------------------------------------------------------------------------------------------
# count1 = 0
# @dp.message_handler(commands=['list'], state=botst.await_third)
# async def questions6(message: Message):
#     global count1
#     lis = []
#     second = 20
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/16img.webp', 'rb'))
#         await bot.send_message(chat_id=id_users, text='Как перевести первый символ строки в верхний регистр?\n🟥 .upper()\n🟦 .title()\n🟨 [0].upper()\n🟩 .lower()', reply_markup=buttons.Quest().quest16())
#         timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
#         lis.append(timer_start_message)
#     for time in range(second-1, 0, -1):
#         for i in range(len(lis)):
#             count1 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i
#for konina in user_id:]    .message_id, text=f'{time}')
# 

# @dp.callback_query_handler(state=botst.await_third)
# async def call(call: CallbackQuery):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count1))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
#         await botst.await_four.set()
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#         await botst.await_four.set()

# #---------------------------------------------------------------------------------------------------
# count2 = 0
# @dp.message_handler(commands=['list'], state=botst.await_four)
# async def questions7(message: Message):
#     global count2
#     lis = []
#     second = 20
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/17img.webp', 'rb'))
#         await bot.send_message(chat_id=id_users, text='Сколько методов в кортеже?\n🟥 2\n🟦 1\n🟨 4\n🟩 3', reply_markup=buttons.Quest().quest17())
#         timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
#         lis.append(timer_start_message)
#     for time in range(second-1, 0, -1):
#         for i in range(len(lis)):
#             count2 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i
#for konina in user_id:]    .message_id, text=f'{time}')
# 

# @dp.callback_query_handler(state=botst.await_four)
# async def call(call: CallbackQuery):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count2))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
     
#         await botst.await_five.set()
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#         await botst.await_five.set()

# #---------------------------------------------------------------------------------------------------
# count3 = 0
# @dp.message_handler(commands=['list'], state=botst.await_five)
# async def questions7(message: Message):
#     global count3
#     lis = []
#     second = 20
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/18img.webp', 'rb'))
#         await bot.send_message(chat_id=id_users, text='Что выведет данная команда?\n🟥 Error\n🟦 False\n🟨 True\n🟩 ()', reply_markup=buttons.Quest().quest18())
#         timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
#         lis.append(timer_start_message)
#     for time in range(second-1, 0, -1):
#         for i in range(len(lis)):
#             count3 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i
#for konina in user_id:]    .message_id, text=f'{time}')
# 

# @dp.callback_query_handler(state=botst.await_five)
# async def call(call: CallbackQuery):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count3))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
     
#         await botst.await_six.set()
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#         await botst.await_six.set()

# #---------------------------------------------------------------------------------------------------
# count4 = 0
# @dp.message_handler(commands=['list'], state=botst.await_six)
# async def questions7(message: Message):
#     global count4
#     lis = []
#     second = 20
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/19img.webp', 'rb'))
#         await bot.send_message(chat_id=id_users, text='Как зовут создателя python?\n🟥 Нирлатотеп\n🟦 Россум\n🟨 Роберт\n🟩 Гвидо', reply_markup=buttons.Quest().quest19())
#         timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
#         lis.append(timer_start_message)
#     for time in range(second-1, 0, -1):
#         for i in range(len(lis)):
#             count4 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i
#for konina in user_id:]    .message_id, text=f'{time}')
# 

# @dp.callback_query_handler(state=botst.await_six)
# async def call(call: CallbackQuery):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count4))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
     
#         await botst.await_seven.set()
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#         await botst.await_seven.set()

# #---------------------------------------------------------------------------------------------------
# count5 = 0
# @dp.message_handler(commands=['list'], state=botst.await_seven)
# async def questions7(message: Message):
#     global count5
#     lis = []
#     second = 20
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/20img.webp', 'rb'))
#         await bot.send_message(chat_id=id_users, text='Каким знаком обозначается остаток от деления нацело?\n🟥 %\n🟦 **\n🟨 //\n🟩 ?!?', reply_markup=buttons.Quest().quest20())
#         timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
#         lis.append(timer_start_message)
#     for time in range(second-1, 0, -1):
#         for i in range(len(lis)):
#             count5 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i
#for konina in user_id:]    .message_id, text=f'{time}')
# 

# @dp.callback_query_handler(state=botst.await_seven)
# async def call(call: CallbackQuery, state):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count5))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
     
#         state.finish()
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#         state.finish()

# #---------------------------------------------------------------------------------------------------
# count1 = 0
# @dp.message_handler(commands=['list'], state=botst.await_third)
# async def questions6(message: Message):
#     global count1
#     lis = []
#     second = 20
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/21img.webp', 'rb'))
#         await bot.send_message(chat_id=id_users, text='Kак обозначается неравенство в Python?\n🟥 <>\n🟦 *сделай неравенство*\n🟨 !=\n🟩 /=', reply_markup=buttons.Quest().quest21())
#         timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
#         lis.append(timer_start_message)
#     for time in range(second-1, 0, -1):
#         for i in range(len(lis)):
#             count1 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i
#for konina in user_id:]    .message_id, text=f'{time}')
# 

# @dp.callback_query_handler(state=botst.await_third)
# async def call(call: CallbackQuery):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count1))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
#         await botst.await_four.set()
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#         await botst.await_four.set()

# #---------------------------------------------------------------------------------------------------
# count2 = 0
# @dp.message_handler(commands=['list'], state=botst.await_four)
# async def questions7(message: Message):
#     global count2
#     lis = []
#     second = 20
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/22img.webp', 'rb'))
#         await bot.send_message(chat_id=id_users, text='Какой набор символов используется для переноса строки ?\n🟥 \p\n🟦 \\n\n🟨 /http\n🟩 /r', reply_markup=buttons.Quest().quest22())
#         timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
#         lis.append(timer_start_message)
#     for time in range(second-1, 0, -1):
#         for i in range(len(lis)):
#             count2 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i
#for konina in user_id:]    .message_id, text=f'{time}')
# 

# @dp.callback_query_handler(state=botst.await_four)
# async def call(call: CallbackQuery):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count2))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
#         await botst.await_five.set()
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#         await botst.await_five.set()

# #---------------------------------------------------------------------------------------------------
# count3 = 0
# @dp.message_handler(commands=['list'], state=botst.await_five)
# async def questions7(message: Message):
#     global count3
#     lis = []
#     second = 20
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/23img.webp', 'rb'))
#         await bot.send_message(chat_id=id_users, text='Целую часть от деления можно найти с помощью?\n🟥 //\n🟦 /\n🟨 %\n🟩 div', reply_markup=buttons.Quest().quest23())
#         timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
#         lis.append(timer_start_message)
#     for time in range(second-1, 0, -1):
#         for i in range(len(lis)):
#             count3 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i
#for konina in user_id:]    .message_id, text=f'{time}')
# 

# @dp.callback_query_handler(state=botst.await_five)
# async def call(call: CallbackQuery):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count3))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
#         await botst.await_six.set()
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#         await botst.await_six.set()

# #---------------------------------------------------------------------------------------------------
# count4 = 0
# @dp.message_handler(commands=['list'], state=botst.await_six)
# async def questions7(message: Message):
#     global count4
#     lis = []
#     second = 20
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/24img.webp', 'rb'))
#         await bot.send_message(chat_id=id_users, text='Сколько значений может принимать строковый тип данных?\n🟥 1\n🟦 2\n🟨 3\n🟩 4', reply_markup=buttons.Quest().quest24())
#         timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
#         lis.append(timer_start_message)
#     for time in range(second-1, 0, -1):
#         for i in range(len(lis)):
#             count4 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i
#for konina in user_id:]    .message_id, text=f'{time}')
# 

# @dp.callback_query_handler(state=botst.await_six)
# async def call(call: CallbackQuery):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count4))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
#         await botst.await_seven.set()
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#         await botst.await_seven.set()

# #---------------------------------------------------------------------------------------------------
# count5 = 0
# @dp.message_handler(commands=['list'], state=botst.await_seven)
# async def questions7(message: Message):
#     global count5
#     lis = []
#     second = 20
#     for id_users in user_id:
#         await bot.send_photo(chat_id=id_users, photo=open('/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/25img.webp', 'rb'))
#         await bot.send_message(chat_id=id_users, text='Команда, выполняющая или не выполняющая действие в зависимости от значения логического условия?\n🟥 Логический тип данных\n🟦 Логическое условие\n🟨 Условный оператор\n🟩 Условное выражение', reply_markup=buttons.Quest().quest25())
#         timer_start_message = await bot.send_message(chat_id=id_users, text='У тебя 20 секунд на ответ . . . ')
#         lis.append(timer_start_message)
#     for time in range(second-1, 0, -1):
#         for i in range(len(lis)):
#             count5 += 1
#             await bot.edit_message_text(chat_id=user_id[i], message_id=lis[i
#for konina in user_id:]    .message_id, text=f'{time}')
# 

# @dp.callback_query_handler(state=botst.await_seven)
# async def call(call: CallbackQuery, state):
#     if call.data == 'True':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Правильно ✅')
#         point = 800 * (1+(1/count5))
#         current_points = nickname_points.get(call.message.chat.id) + int(point)
#         nickname_points.update({call.message.chat.id: current_points})
#         state.finish()
#     elif call.data == 'False':
#         await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
#         await bot.send_message(chat_id=call.message.chat.id, text='Ты проиграл ❌')
#         state.finish()




if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)
