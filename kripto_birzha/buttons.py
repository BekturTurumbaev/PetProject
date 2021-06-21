from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


class Number:
    def number(self):
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

        button2 = KeyboardButton(text='Отправить номер телефона... 📱', request_contact=True)

        markup.add(button2)
        return markup

class Log:
    def osnov(self):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='Купить монеты', callback_data='buy')
        button2 = InlineKeyboardButton(text='Продать монеты', callback_data='sell')
        button3 = InlineKeyboardButton(text='Посмотреть МОИ транзакции', callback_data='see')
        button4 = InlineKeyboardButton(text='Удалить аккаунт', callback_data='remove')
        button5 = InlineKeyboardButton(text='Просмотреть курс валют', callback_data='view')
        button6 = InlineKeyboardButton(text='Мой баланс', callback_data='bal')
        button7 = InlineKeyboardButton(text='Моя крипта', callback_data='krip')
        markup.add(button1, button2)
        markup.add(button3, button4)
        markup.add(button6, button7)
        markup.add(button5)
        return markup

