import psycopg2

links = [
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/1img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/2img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/3img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/4img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/5img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/6img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/7img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/8img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/9img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/10img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/11img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/12img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/13img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/14img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/15img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/16img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/17img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/18img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/19img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/20img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/21img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/22img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/23img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/24img.webp',
'/home/asus/Desktop/Мучительные_две_недели/kahoot_bot/img_kahoot/25img.webp']

qwerty = [
'Что выведет данная команда?',
'Python это змея?',
'Какого знака не может быть в переменной?',
'Что выведет данная команда?',
'Какие цвета на лого python?',
'Что выведет данная команда?',
'Что выведет данная команда?',
'Создатель python человек?',
'Что выведет данная команда?',
'Что выведет данная команда?',
'Python - интерпретируемый язык или компилируемый?',
'Сколько видов импорта сущуствует?',
'Можно ли создать декоратор из класса?',
'Можно ли использовать несколько декораторов для одной функции?',
'Как пишутся комментарии в питоне?',
'Как перевести первый символ строки в верхний регистр?',
'Сколько методов в кортеже?',
'Что выведет данная команда?',
'Как зовут создателя python?',
'Каким знаком обозначается остаток от деления нацело?',
'Kак обозначается неравенство в Python?',
'Какой набор символов используется для переноса строки ?',
'Целую часть от деления можно найти с помощью?',
'Сколько значений может принимать строковый тип данных?',
'Команда, выполняющая или не выполняющая действие в зависимости от значения логического условия?']

answers = [
'🟥 3 + 2\n🟦 (5)\n🟨 5\n🟩 SyntaxError',
'🟥 True\n🟦 False',
'🟥 -\n🟦 Цифры\n🟨 _\n🟩 Буквы',
'🟥 1\n🟦 a\n🟨 b\n🟩 Error',
'🟥 Фиолетовый-Черный\n🟦 Синий-Зеленый\n🟨 Явно змея\n🟩 Желтый-Синий',
'🟥 От 1 до 100\n🟦 i 100 раз\n🟨 Error\n🟩 От 0 до 99',
'🟥 (abc)\n🟦 abc\n🟨 a+b+c\n🟩 Error',
'🟥 True\n🟦 False',
'🟥 TypeError\n🟦 274, 2\n🟨 274 + 2\n🟩 NameError',
'🟥 True\n🟦 False\n🟨 TypeError\n🟩 1',
'🟥 Интерпретируемый язык\n🟦 Компилируемый язык',
'🟥 4\n🟦 1\n🟨 2\n🟩 3',
'🟥 True\n🟦 False',
'🟥 True\n🟦 False',
'🟥 @\n🟦 #\n🟨 *\n🟩 +',
'🟥 .upper()\n🟦 .title()\n🟨 [0].upper()\n🟩 .lower()',
'🟥 2\n🟦 1\n🟨 4\n🟩 3',
'🟥 Error\n🟦 False\n🟨 True\n🟩 ()',
'🟥 Нирлатотеп\n🟦 Россум\n🟨 Роберт\n🟩 Гвидо',
'🟥 %\n🟦 **\n🟨 //\n🟩 ?!?',
'🟥 <>\n🟦 *сделай неравенство*\n🟨 !=\n🟩 /=',
'🟥 \p\n🟦 \\n\n🟨 /http\n🟩 /r',
'🟥 //\n🟦 /\n🟨 %\n🟩 div',
'🟥 1\n🟦 2\n🟨 3\n🟩 4',
'🟥 Логический тип данных\n🟦 Логическое условие\n🟨 Условный оператор\n🟩 Условное выражение']

answers = [
'🟥 3 + 2\n🟦 (5)\n🟨 5\n🟩 SyntaxError',
'🟥 True\n🟦 False',
'🟥 -\n🟦 Цифры\n🟨 _\n🟩 Буквы',
'🟥 1\n🟦 a\n🟨 b\n🟩 Error',
'🟥 Фиолетовый-Черный\n🟦 Синий-Зеленый\n🟨 Явно змея\n🟩 Желтый-Синий',
'🟥 От 1 до 100\n🟦 i 100 раз\n🟨 Error\n🟩 От 0 до 99',
'🟥 (abc)\n🟦 abc\n🟨 a+b+c\n🟩 Error',
'🟥 True\n🟦 False',
'🟥 TypeError\n🟦 274, 2\n🟨 274 + 2\n🟩 NameError',
'🟥 True\n🟦 False\n🟨 TypeError\n🟩 1',
'🟥 Интерпретируемый язык\n🟦 Компилируемый язык',
'🟥 4\n🟦 1\n🟨 2\n🟩 3',
'🟥 True\n🟦 False',
'🟥 True\n🟦 False',
'🟥 @\n🟦 #\n🟨 *\n🟩 +',
'🟥 .upper()\n🟦 .title()\n🟨 [0].upper()\n🟩 .lower()',
'🟥 2\n🟦 1\n🟨 4\n🟩 3',
'🟥 Error\n🟦 False\n🟨 True\n🟩 ()',
'🟥 Нирлатотеп\n🟦 Россум\n🟨 Роберт\n🟩 Гвидо',
'🟥 %\n🟦 **\n🟨 //\n🟩 ?!?',
'🟥 <>\n🟦 *сделай неравенство*\n🟨 !=\n🟩 /=',
'🟥 \p\n🟦 \\n\n🟨 /http\n🟩 /r',
'🟥 //\n🟦 /\n🟨 %\n🟩 div',
'🟥 1\n🟦 2\n🟨 3\n🟩 4',
'🟥 Логический тип данных\n🟦 Логическое условие\n🟨 Условный оператор\n🟩 Условное выражение']

# 🟥🟦🟨🟩

bd_password = input("Введите пароль от Базы Данных: ")


conn = psycopg2.connect(
dbname='postgres', 
user='postgres', 
password=bd_password, 
host='localhost'
)

cursor = conn.cursor()

cursor.execute('''CREATE TABLE question(
id SERIAL PRIMARY KEY, 
link VARCHAR(200) NOT NULL,
quest VARCHAR(150) NOT NULL,
variant VARCHAR(100) NOT NULL,
answer VARCHAR(20) NOT NULL);'''
)

query = '''INSERT INTO question(link, quest, variant, answer) VALUES '''

for index in range(len(links)):
        query += f'(\'{links[index]}\', \'{qwerty[index]}\', \'{answers[index]}\'),'

sql_query = query[:-1] + ';'

cursor.execute(sql_query)
conn.commit()

cursor.close()
conn.close()

########################################################################


# a = {
#         'haha': 0,
#         'koko': 1
# }
# a.update({'brgj': 92189})


# print(a.get('haha'))
# print(b[0])






# # Основа
# from os import remove
# from typing import Text
# from aiogram import Bot
# from aiogram.dispatcher import Dispatcher
# from aiogram import executor
# from aiogram.types import Message, ParseMode, document, mask_position, message, CallbackQuery, user
# from aiogram.dispatcher.filters import state
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# # Второстепенные
# import random

# from aiohttp.helpers import rfc822_formatted_time
# import config
# import pathlib
# import time
# import buttons

# storage = MemoryStorage()

# bot = Bot(token=config.TOKEN)
# dp = Dispatcher(bot=bot, storage=storage)

# user_id = [841478320, 707051892, 1039874926]

# @dp.message_handler()
# async def is_ready_player(message: Message):
#     await bot.send_message(chat_id=user_id, text='Host')
# #     await bot.send_photo(chat_id=message.chat.id, photo=open('/home/asus/Desktop/kahoot_bot/img_kahoot.py/1img.webp', 'rb'))





# if __name__ == "__main__":
#     executor.start_polling(dispatcher=dp)





# PATH = pathlib.Path(__file__).parent
# pin = random.randrange(2001000, 3000000)

# @dp.message_handler(state=states.is_ready)
# async def is_ready_player(message: Message):
#     if message.text == 'Готов!':
#         postgres.update(
#             ['player_is_ready', ],
#             [1],
#             ('player_telegram_id', message.from_user.id),
#             'players'
#         )
#         await message.answer(text='Игра начнётся через 30 секунд!')

#         for s in range(30):
#             await asyncio.sleep(1)
#             await message.edit_text(text=f'{s}')

#         return await states.game_started.set()
#     else:
#         await message.answer(text='Если вы готовы нажмите "Готов!"', reply_markup=tbtns.ready_btn())


# @dp.message_handler(state=states.game_started)
# async def start_game(message: Message):
#     get_users = postgres.select(['*'], ['players'])

#     for user in get_users:
#         await bot.send_message(chat_id=user[1], text='Как зовут создателя Python?')



# @dp.message_handler(commands=['hope'])
# async def first(message):
#     a = 20
#     for i in range(20):
#         if a <= 0:
#             pass
#         else:
#             time.sleep(1)
#             await bot.send_message(message.chat.id, a)
#             await bot.delete_message(message.chat.id, message.message_id-1)
        # a-=1



# if __name__ == "__main__":
#     executor.start_polling(dispatcher=dp)






# @dp.message_handler(commands=['hope'])
# async def first(message):
#     a = 20
#     for i in range(20):
#         time.sleep(1)
#         await message.answer(text='1 or 2', reply_markup=buttons.Quest().quest1())
#         await message.answer(text=a)
#         a -= 1






# from random import triangular


# import random
# for i in range(2):
#     words = {
#         '5': 'Что выведет данная команда?',
#         'False': 'Python это змея?',
#         '-': 'Какого знака не может быть в переменной?',
#         'Error': 'Что выведет данная команда?',
#         'Желтый-Синий': 'Какие цвета на лого python?'
#         }
#     word = random.choice(tuple(words.keys()))
#     peremen = words.get(word)
#     print(peremen)
#     words.pop(word)
# print(len(words))

#1
# 3 + 2
# (5)
# 5
# SyntaxError

#2
# True
# False

#3
# -
# Цифры
# _
# Буквы

#4
# 1
# a
# b
# Error

#5
# Фиолетовый-Черный
# Синий-Зеленый
# Явно змея
# Желтый-Синий

#6
# Что выведет данная команда?
#
# От 1 до 100
# i 100 раз
# Error
# От 0 до 99













# a = [1,2,3,4,1,0]
# op = []
# op.append(list(a))
# print(op)

# import pathlib
# PATH = pathlib.Path(__file__).parent
# print(PATH)

# a = "это пример строки....wow!!!"
# print (a.startswith('это'))
# print (a.startswith('пример' ))

# VPN MinorRoosterLegislator

# import os
# path = '/home/asus/Desktop/Всячина/neon'
# link = 'https://images.wallpaperscraft.ru/image/nochnoj_gorod_vyveski_neon_139551_1280x720.jpg'
# link = 'https://images.wallpaperscraft.ru/image/nochnoj_gorod_ulitsa_zont_121639_1280x720.jpg'
# link = 'https://wallscloud.net/uploads/cache/243973293/peizazh-gory-neonovaia-luna-neonovaia-reka-neonovye-gory-neo_(1)-1024x576-MM-90.jpg'
# img = os.system(f'wget {link} -P {path}') 