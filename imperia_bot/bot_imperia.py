from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram import executor
from aiogram.types import Message, ParseMode, document, mask_position, message, CallbackQuery, user, ReplyKeyboardRemove
from aiogram.dispatcher.filters import state
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import psycopg2
import random
import config
import pathlib
import buttons
from states import BotStates
import selec

botst = BotStates()
storage = MemoryStorage()

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

conn = psycopg2.connect(
    dbname='imperia', 
    user='postgres', 
    password='05052005', 
    host='localhost')
cursor = conn.cursor()

@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer(text='Добро пожаловать в Империю пиц!', reply_markup=buttons.Main().mains())
    await botst.await_first.set()


@dp.callback_query_handler(state=botst.await_first)
async def call(call: CallbackQuery, state):
    #Menu
    if call.data == 'menu':
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы выйти, нажмите "назад"', reply_markup=buttons.Main().retur1())
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=buttons.Main().menu())
    
    elif call.data == 'ret1':
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы выйти, нажмите "назад"', reply_markup=buttons.Main().mains())

    elif call.data == 'ret2':
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы выйти, нажмите "назад"', reply_markup=buttons.Vakancies().vaka())

    elif call.data == 'ret3':
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы выйти, нажмите "назад"', reply_markup=buttons.Main().menu())

    elif call.data == 'break':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        main1 = selec.breakfast()
        price11 = [o for o in buttons.Price().price1()]
        for ind in range(len(main1[0])):
            await bot.send_message(chat_id=call.message.chat.id, text=main1[0][ind])
            await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'/home/asus/Desktop/imperia/menu_img/breakfast/{main1[1][ind]}', 'rb'), reply_markup=price11[ind])
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы выйти, нажмите "назад"', reply_markup=buttons.Main().retur1())

    elif call.data == 'pizza':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        main1 = selec.pizza()
        price22 = [o for o in buttons.Price().price2()]
        for ind in range(len(main1[0])):
            await bot.send_message(chat_id=call.message.chat.id, text=main1[0][ind])
            await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'/home/asus/Desktop/imperia/menu_img/pizza_40_cm/{main1[1][ind]}', 'rb'), reply_markup=price22[ind])
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы выйти, нажмите "назад"', reply_markup=buttons.Main().retur1())

    elif call.data == 'roll':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        main1 = selec.roll()
        price33 = [o for o in buttons.Price().price3()]
        for ind in range(len(main1[0])):
            await bot.send_message(chat_id=call.message.chat.id, text=main1[0][ind])
            await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'/home/asus/Desktop/imperia/menu_img/rolls/{main1[1][ind]}', 'rb'), reply_markup=price33[ind])
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы выйти, нажмите "назад"', reply_markup=buttons.Main().retur1())

    elif call.data == 'salad':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        main1 = selec.salad()
        price44 = [o for o in buttons.Price().price4()]
        for ind in range(len(main1[0])):
            await bot.send_message(chat_id=call.message.chat.id, text=main1[0][ind])
            await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'/home/asus/Desktop/imperia/menu_img/salads/{main1[1][ind]}', 'rb'), reply_markup=price44[ind])
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы выйти, нажмите "назад"', reply_markup=buttons.Main().retur1())

    elif call.data == 'snack':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        main1 = selec.snack()
        price55 = [o for o in buttons.Price().price5()]
        for ind in range(len(main1[0])):
            await bot.send_message(chat_id=call.message.chat.id, text=main1[0][ind])
            await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'/home/asus/Desktop/imperia/menu_img/snacks/{main1[1][ind]}', 'rb'), reply_markup=price55[ind])
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы выйти, нажмите "назад"', reply_markup=buttons.Main().retur1())



    #Shares
    elif call.data == 'ak':
        cmd_0 = 'SELECT headers,description FROM share'
        cursor.execute(cmd_0)
        table_name = cursor.fetchall()

        cmd_11 = 'SELECT images FROM share'
        cursor.execute(cmd_11)
        img = cursor.fetchall()
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        for i in range(len(table_name)):
            await bot.send_photo(chat_id=call.message.chat.id, photo=open(f'/home/asus/Desktop/imperia/shares_img/{img[i]}'.replace(')','').replace('(','').replace("'",'').replace(',',''), 'rb'))
            await bot.send_message(chat_id=call.message.chat.id, text=str(table_name[i]).replace("'",'').replace('(','').replace(')',''))
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы выйти, нажмите "назад"', reply_markup=buttons.Main().retur1())
    
    #Vakancies
    elif call.data == 'vak':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=buttons.Vakancies().vaka())

    elif call.data == 'vakas':
        await bot.send_message(chat_id=call.message.chat.id, text=selec.sta()[0])
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=buttons.Vakancies().vtoroe())
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы выйти, нажмите "назад"', reply_markup=buttons.Main().retur1())

    elif call.data == 'vak1':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text=selec.sta()[1])
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы выйти, нажмите "назад"', reply_markup=buttons.Main().retur2())

    elif call.data == 'vak2':
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        await bot.send_message(chat_id=call.message.chat.id, text=selec.sta()[2])
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы выйти, нажмите "назад"', reply_markup=buttons.Main().retur2())
    #Company
    elif call.data == 'comp':
        cmd_1 = 'SELECT * FROM share'
        cursor.execute(cmd_1)
        table_name = cursor.fetchall()
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        for com in table_name:
            await bot.send_message(chat_id=call.message.chat.id, text=str(com).replace("'",'').replace('(','').replace(')',''))
        await bot.send_message(chat_id=call.message.chat.id, text='Чтобы выйти, нажмите "назад"', reply_markup=buttons.Main().retur1())










if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)


cursor.close()
conn.close()
