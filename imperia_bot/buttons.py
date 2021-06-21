from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import psycopg2
import selec

conn = psycopg2.connect(
    dbname='imperia', 
    user='postgres', 
    password='', 
    host='localhost')
cursor = conn.cursor()

class Main:
    def retur1(self):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='Назад', callback_data='ret1')
        markup.add(button1)
        return markup

    def retur2(self):
        markup = InlineKeyboardMarkup()
        button2 = InlineKeyboardButton(text='Назад', callback_data='ret2')
        markup.add(button2)
        return markup

    def retur3(self):
        markup = InlineKeyboardMarkup()
        button3 = InlineKeyboardButton(text='Назад', callback_data='ret3')
        markup.add(button3)
        return markup

    def mains(self):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='Меню 📜', callback_data='menu')
        button2 = InlineKeyboardButton(text='Акции 📉', callback_data='ak')
        button3 = InlineKeyboardButton(text='Вакансии 💰', callback_data='vak')
        button4 = InlineKeyboardButton(text='О компании 🗄', callback_data='comp')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup

    def menu(self):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='Завтраки 🍳', callback_data='break')
        button2 = InlineKeyboardButton(text='Пицца 40 см 🍕', callback_data='pizza')
        button3 = InlineKeyboardButton(text='Роллы 🍱', callback_data='roll')
        button4 = InlineKeyboardButton(text='Салаты 🥗', callback_data='salad')
        button5 = InlineKeyboardButton(text='Закуски 🍢', callback_data='snack')
        markup.add(button1)
        markup.add(button2)
        markup.add(button3)
        markup.add(button4)
        markup.add(button5)
        return markup

class Vakancies:
    def vaka(self):
        cmd_0 = 'SELECT headers FROM vacancies'
        cursor.execute(cmd_0)
        table_name = cursor.fetchall()
        ans = str(table_name[0]).replace("'","").replace('(','').replace(')','').replace(',','')
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text=f"{ans}", callback_data='vakas')
        markup.add(button1)

        return markup

    def vtoroe(self):
        cmd_0 = 'SELECT headers FROM vacancies'
        cursor.execute(cmd_0)
        table_name = cursor.fetchall()
        ans1 = str(table_name[1]).replace("'","").replace('(','').replace(')','').replace(',','')
        ans2 = str(table_name[2]).replace("'","").replace('(','').replace(')','').replace(',','')
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text=f"{ans1}", callback_data='vak1')
        button2 = InlineKeyboardButton(text=f"{ans2}", callback_data='vak2')
        markup.add(button1, button2)

        return markup

class Price:
    def price1(self):
        p = selec.breakfast()[2]
        for pr in p:
            markup = InlineKeyboardMarkup()
            button1 = InlineKeyboardButton(text=f"{pr}", callback_data=0)
            markup.add(button1)
            yield markup
    def price2(self):
        p = selec.pizza()[2]
        for pr in p:
            markup = InlineKeyboardMarkup()
            button1 = InlineKeyboardButton(text=f"{pr}", callback_data=0)
            markup.add(button1)
            yield markup
    def price3(self):
        p = selec.roll()[2]
        for pr in p:
            markup = InlineKeyboardMarkup()
            button1 = InlineKeyboardButton(text=f"{pr}", callback_data=0)
            markup.add(button1)
            yield markup
    def price4(self):
        p = selec.salad()[2]
        for pr in p:
            markup = InlineKeyboardMarkup()
            button1 = InlineKeyboardButton(text=f"{pr}", callback_data=0)
            markup.add(button1)
            yield markup
    def price5(self):
        p = selec.snack()[2]
        for pr in p:
            markup = InlineKeyboardMarkup()
            button1 = InlineKeyboardButton(text=f"{pr}", callback_data=0)
            markup.add(button1)
            yield markup



    # def vacancies(self):
    #     markup = InlineKeyboardMarkup()
    #     button1 = InlineKeyboardButton(text='Завтраки 🍳', callback_data='menu')
    #     button2 = InlineKeyboardButton(text='Пицца 40 см 🍕', callback_data='ak')
    #     button3 = InlineKeyboardButton(text='Роллы 🍱', callback_data='vak')
    #     button4 = InlineKeyboardButton(text='Салаты 🥗', callback_data='comp')
    #     button5 = InlineKeyboardButton(text='Закуски 🍢', callback_data='comp')
    #     markup.add(button1)
    #     markup.add(button2)
    #     markup.add(button3)
    #     markup.add(button4)
    #     markup.add(button5)
    #     return markup