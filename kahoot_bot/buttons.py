from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class Ready:
    def readys(self):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text="Готов ✅", callback_data="1")
        button2 = InlineKeyboardButton(text="Не готов ❌", callback_data="0")
        markup.add(button1, button2)
        return markup


class Quest:
    def generate_buttons(self, arguments):
        markup = InlineKeyboardMarkup(row_width=2)
        button1 = InlineKeyboardButton(text=arguments[0][0], callback_data=str(arguments[0][1]))
        button2 = InlineKeyboardButton(text=arguments[1][0], callback_data=str(arguments[1][1]))
        markup.add(button1, button2)
        if len(arguments) == 4:
            button3 = InlineKeyboardButton(text=arguments[2][0], callback_data=str(arguments[2][1]))
            button4 = InlineKeyboardButton(text=arguments[3][0], callback_data=str(arguments[3][1]))
            markup.add(button3, button4)

        return markup
