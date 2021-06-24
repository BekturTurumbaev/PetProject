from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram import executor
from aiogram.types import Message, CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage
####
import time
from imperia import all_pars
import multiprocessing
import os
import psycopg2
import config
import buttons
from states import BotStates
import selec
import pathlib

PATH = pathlib.Path(__file__).parent

botst = BotStates()
storage = MemoryStorage()

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

dbname = input("Your database name: ")
dbuser = input("Your database user: ")
dbpswd = input("Your database password: ")

conn = psycopg2.connect(
    dbname=dbname, 
    user=dbuser, 
    password=dbpswd, 
    host='localhost')
cursor = conn.cursor()

@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer(text='Добро пожаловать в Империю пиц!', reply_markup=buttons.Main().mains())
    await botst.await_first.set()


@dp.callback_query_handler(state=botst.await_first)
async def call_main(call: CallbackQuery, state):
    #Menu
    if call.data == 'menu':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=buttons.Main().menu())
        await botst.await_second.set()

    #Shares
    elif call.data == 'ak':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        cmd_0 = 'SELECT headers,description ,id FROM share'
        cursor.execute(cmd_0)
        name_descr = cursor.fetchall()
        cmd_11 = 'SELECT images FROM share'
        cursor.execute(cmd_11)
        img = cursor.fetchall()
        for i in range(len(name_descr)):
            await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'{PATH}/imperia/shares_img/{img[i][0]}', 'rb'))
            await bot.send_message(chat_id = call.message.chat.id, text=name_descr[i][0], reply_markup=buttons.Shares().more(name_descr[i][-1]))
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы вернуться в главное меню, нажмите "назад".', reply_markup=buttons.Shares().retarun())
        await botst.await_third.set()
    
    #Vakancies
    elif call.data == 'vak':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=buttons.Vakancies().vaka())
        await botst.await_four.set()

    #Company
    elif call.data == 'comp':
        cmd_1 = 'SELECT * FROM company'
        cursor.execute(cmd_1)
        company_desc = cursor.fetchall()
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        for com in company_desc:
            await bot.send_message(chat_id=call.message.chat.id, text=f'{com[0]} {com[1]}', reply_markup=buttons.Company().more_company(com[0]))
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы вернуться в главное меню, нажмите "назад".', reply_markup=buttons.Shares().retarun())
        await botst.await_six.set()

@dp.callback_query_handler(state=botst.await_second)
async def calling1(call: CallbackQuery):
    if call.data == 'break':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        main1 = selec.breakfast()
        price11 = [o for o in buttons.Price().price1()]
        for ind in range(len(main1[0])):
            await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'{PATH}/imperia/menu_img/breakfast/{main1[1][ind]}', 'rb'), caption=main1[0][ind], reply_markup=price11[ind])
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы вернуться к мену, нажмите "назад".', reply_markup=buttons.Main().retur())

    elif call.data == 'pizza':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        main1 = selec.pizza()
        price22 = [o for o in buttons.Price().price2()]
        for ind in range(len(main1[0])):
            await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'{PATH}/imperia/menu_img/pizza_40_cm/{main1[1][ind]}', 'rb'), caption=main1[0][ind], reply_markup=price22[ind])
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы вернуться к мену, нажмите "назад".', reply_markup=buttons.Main().retur())

    elif call.data == 'roll':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        main1 = selec.roll()
        price33 = [o for o in buttons.Price().price3()]
        for ind in range(len(main1[0])):
            await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'{PATH}/imperia/menu_img/rolls/{main1[1][ind]}', 'rb'), caption=main1[0][ind], reply_markup=price33[ind])
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы вернуться к мену, нажмите "назад".', reply_markup=buttons.Main().retur())

    elif call.data == 'salad':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        main1 = selec.salad()
        price44 = [o for o in buttons.Price().price4()]
        for ind in range(len(main1[0])):
            await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'{PATH}/imperia/menu_img/salads/{main1[1][ind]}', 'rb'), caption=main1[0][ind], reply_markup=price44[ind])
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы вернуться к мену, нажмите "назад".', reply_markup=buttons.Main().retur())

    elif call.data == 'snack':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        main1 = selec.snack()
        price55 = [o for o in buttons.Price().price5()]
        for ind in range(len(main1[0])):
            await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'{PATH}/imperia/menu_img/snacks/{main1[1][ind]}', 'rb'), caption=main1[0][ind], reply_markup=price55[ind])
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы вернуться к мену, нажмите "назад".', reply_markup=buttons.Main().retur())

    elif call.data == 'return':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=buttons.Main().mains())
        await botst.await_first.set()

    elif call.data == 'return_menu':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=buttons.Main().menu())
        await botst.await_second.set()

@dp.callback_query_handler(state=botst.await_third)
async def calling2(call: CallbackQuery):
    if call.data == 'return_main_menu':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=buttons.Main().mains())
        await botst.await_first.set()
    else:
        cmd_080 = f'SELECT description FROM share WHERE id = {call.data}'
        cursor.execute(cmd_080)
        description = cursor.fetchone()
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'{description[0]}', reply_markup=None)


@dp.callback_query_handler(state=botst.await_four)
async def calling2(call: CallbackQuery):
    if call.data == 'vakas':
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=selec.sta()[0], reply_markup=buttons.Vakancies().vtoroe())
        await botst.await_five.set()
    elif call.data == 'ret':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=buttons.Main().mains())
        await botst.await_first.set()

@dp.callback_query_handler(state=botst.await_five)
async def calling2(call: CallbackQuery):
    if call.data == 'vak1':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text=selec.sta()[1])
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы выйти, нажмите "назад"', reply_markup=buttons.Vakancies().return_vakan())

    elif call.data == 'vak2':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text=selec.sta()[2])
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы выйти, нажмите "назад"', reply_markup=buttons.Vakancies().return_vakan())

    elif call.data == 'return_main_vakancies':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=buttons.Vakancies().vaka())
        await botst.await_four.set()

    elif call.data == 'return_vakan':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=buttons.Vakancies().vtoroe())
        await botst.await_five.set()

@dp.callback_query_handler(state=botst.await_six)
async def calling2(call: CallbackQuery):
    if call.data == 'return_main_menu':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=buttons.Main().mains())
        await botst.await_first.set()
    else:
        cmd_000 = f'SELECT headers, description FROM company WHERE id = {call.data}'
        cursor.execute(cmd_000)
        description = cursor.fetchone()
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'{description[0]} {description[1]}', reply_markup=None)


# All files run in the multiprocessing

# def install():
#     while True:
#         time.sleep(100)
#         os.system(f'wget -c -r -k -l 7 -p -E -nc https://mypizza.kg/ -P {PATH}')

# if __name__ == "__main__":
#     program1 = multiprocessing.Process(target=executor.start_polling, args=(dp,))
#     program2 = multiprocessing.Process(target=all_pars.zapusk1, args=(all_pars.Scraper_main(),))
#     program3 = multiprocessing.Process(target=all_pars.zapusk2, args=(all_pars.Shares(),))
#     program4 = multiprocessing.Process(target=all_pars.zapusk3, args=(all_pars.Company(),))
#     program5 = multiprocessing.Process(target=all_pars.zapusk4, args=(all_pars.Vacancies(),))
#     program6 = multiprocessing.Process(target=install)

#     program6.start()


#     program2.start()
#     program3.start()
#     program4.start()
#     program5.start()

#     time.sleep(60)
#     program1.start()
