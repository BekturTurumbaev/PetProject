from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import psycopg2
import selec

dbname = input("Your database name: ")
dbuser = input("Your database user: ")
dbpswd = input("Your database password: ")

conn = psycopg2.connect(
    dbname=dbname, 
    user=dbuser, 
    password=dbpswd, 
    host='localhost')
cursor = conn.cursor()

class Main:
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
        button6 = InlineKeyboardButton(text='Назад ↩️', callback_data='return')
        markup.add(button1)
        markup.add(button2)
        markup.add(button3)
        markup.add(button4)
        markup.add(button5)
        markup.add(button6)
        return markup

    def retur(self):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='Назад ↩️', callback_data='return_menu')
        markup.add(button1)
        return markup

class Shares:
    def more(self, i):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='Подробнее.', callback_data=f'{i}')
        markup.add(button1)

        return markup

    def retarun(self):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='Назад ↩️', callback_data='return_main_menu')
        markup.add(button1)
        return markup

class Vakancies:
    def vaka(self):
        cmd_0 = 'SELECT headers FROM vacancies;'
        cursor.execute(cmd_0)
        table_name = cursor.fetchone()
        ans = table_name[0]
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text=f"{ans}", callback_data='vakas')
        button2 = InlineKeyboardButton(text="Назад ↩️", callback_data='ret')
        markup.add(button1)
        markup.add(button2)

        return markup

    def vtoroe(self):
        cmd_0 = 'SELECT headers FROM vacancies'
        cursor.execute(cmd_0)
        table_name = cursor.fetchall()
        ans1 = table_name[1][0]
        ans2 = table_name[2][0].strip()
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text=f"{ans1}", callback_data='vak1')
        button2 = InlineKeyboardButton(text=f"{ans2}", callback_data='vak2')
        button3 = InlineKeyboardButton(text="Назад ↩️", callback_data='return_main_vakancies')
        markup.add(button1, button2)
        markup.add(button3)

        return markup

    def return_vakan(self):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='Назад ↩️', callback_data='return_vakan')
        markup.add(button1)
        return markup

class Company:
    def more_company(self, i):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='Подробнее.', callback_data=f'{i}')
        markup.add(button1)
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