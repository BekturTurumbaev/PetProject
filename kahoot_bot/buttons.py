from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
class Ready:
    def readys(self):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='Готов ✅', callback_data='1')
        button2 = InlineKeyboardButton(text='Не готов ❌', callback_data='0')
        markup.add(button1, button2)
        return markup
class Quest:
    def quest1(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='False')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        button3 = InlineKeyboardButton(text='🟨', callback_data='True')
        button4 = InlineKeyboardButton(text='🟩', callback_data='False')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup
    def quest2(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='True')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        markup.add(button1, button2)
        return markup
    def quest3(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='True')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        button3 = InlineKeyboardButton(text='🟨', callback_data='False')
        button4 = InlineKeyboardButton(text='🟩', callback_data='False')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup
    def quest4(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='False')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        button3 = InlineKeyboardButton(text='🟨', callback_data='False')
        button4 = InlineKeyboardButton(text='🟩', callback_data='True')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup
    def quest5(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='False')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        button3 = InlineKeyboardButton(text='🟨', callback_data='False')
        button4 = InlineKeyboardButton(text='🟩', callback_data='True')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup
    def quest6(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='False')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        button3 = InlineKeyboardButton(text='🟨', callback_data='True')
        button4 = InlineKeyboardButton(text='🟩', callback_data='False')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup
    def quest7(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='False')
        button2 = InlineKeyboardButton(text='🟦', callback_data='True')
        button3 = InlineKeyboardButton(text='🟨', callback_data='False')
        button4 = InlineKeyboardButton(text='🟩', callback_data='False')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup
    def quest8(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='True')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        markup.add(button1, button2)
        return markup
    def quest9(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='True')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        button3 = InlineKeyboardButton(text='🟨', callback_data='False')
        button4 = InlineKeyboardButton(text='🟩', callback_data='False')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup
    def quest10(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='False')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        button3 = InlineKeyboardButton(text='🟨', callback_data='True')
        button4 = InlineKeyboardButton(text='🟩', callback_data='False')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup
    def quest11(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='True')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        markup.add(button1, button2)
        return markup
    def quest12(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='True')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        button3 = InlineKeyboardButton(text='🟨', callback_data='False')
        button4 = InlineKeyboardButton(text='🟩', callback_data='False')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup
    def quest13(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='True')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        markup.add(button1, button2)
        return markup
    def quest14(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='True')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        markup.add(button1, button2)
        return markup
    def quest15(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='False')
        button2 = InlineKeyboardButton(text='🟦', callback_data='True')
        button3 = InlineKeyboardButton(text='🟨', callback_data='False')
        button4 = InlineKeyboardButton(text='🟩', callback_data='False')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup
    def quest16(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='False')
        button2 = InlineKeyboardButton(text='🟦', callback_data='True')
        button3 = InlineKeyboardButton(text='🟨', callback_data='False')
        button4 = InlineKeyboardButton(text='🟩', callback_data='False')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup
    def quest17(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='True')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        button3 = InlineKeyboardButton(text='🟨', callback_data='False')
        button4 = InlineKeyboardButton(text='🟩', callback_data='False')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup
    def quest18(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='False')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        button3 = InlineKeyboardButton(text='🟨', callback_data='False')
        button4 = InlineKeyboardButton(text='🟩', callback_data='True')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup
    def quest19(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='False')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        button3 = InlineKeyboardButton(text='🟨', callback_data='False')
        button4 = InlineKeyboardButton(text='🟩', callback_data='True')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup
    def quest20(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='False')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        button3 = InlineKeyboardButton(text='🟨', callback_data='True')
        button4 = InlineKeyboardButton(text='🟩', callback_data='False')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup
    def quest21(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='False')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        button3 = InlineKeyboardButton(text='🟨', callback_data='True')
        button4 = InlineKeyboardButton(text='🟩', callback_data='False')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup
    def quest22(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='False')
        button2 = InlineKeyboardButton(text='🟦', callback_data='True')
        button3 = InlineKeyboardButton(text='🟨', callback_data='False')
        button4 = InlineKeyboardButton(text='🟩', callback_data='False')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup
    def quest23(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='True')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        button3 = InlineKeyboardButton(text='🟨', callback_data='False')
        button4 = InlineKeyboardButton(text='🟩', callback_data='True')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup
    def quest24(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='False')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        button3 = InlineKeyboardButton(text='🟨', callback_data='False')
        button4 = InlineKeyboardButton(text='🟩', callback_data='True')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup
    def quest25(self, argument):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton(text='🟥', callback_data='False')
        button2 = InlineKeyboardButton(text='🟦', callback_data='False')
        button3 = InlineKeyboardButton(text='🟨', callback_data='True')
        button4 = InlineKeyboardButton(text='🟩', callback_data='False')
        markup.add(button1, button2)
        markup.add(button3, button4)
        return markup