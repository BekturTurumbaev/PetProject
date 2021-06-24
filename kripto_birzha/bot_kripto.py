import re
import time
import random
import socket
import smtplib
import multiprocessing
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


import dns.resolver
from aiogram import Bot
from aiogram import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import db
import config
import buttons
from states import BotStates


botst = BotStates()
storage = MemoryStorage()

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

@dp.message_handler(commands=["start"])
async def start(message: Message):
    cmd_080 = f"DELETE FROM login WHERE phone_number = '';"
    db.cursor.execute(cmd_080)
    db.conn.commit()
    cmd_5 = f"SELECT phone_number FROM login WHERE tg_id = {message.chat.id};"
    db.cursor.execute(cmd_5)
    teg_id = db.cursor.fetchone()
    if teg_id:
        await message.answer(
            text="О, вы были зарегестрированы. \nДавайте продолжим.",
            reply_markup=buttons.Log().osnov(),
        )
        await botst.await_six.set()
    else:
        await message.answer(
            text="Добро пожаловать! \nВведите свое имя. \nИмя может содержать только буквы и один пробел! \nМинимальное количество символов 2, максимальное 20: "
        )
        await botst.await_first.set()


@dp.message_handler(state=botst.await_first)
async def reqistr1(message: Message):
    if message.text:
        if (
            message.text.replace(" ", "").isalpha()
            and message.text.count(" ") <= 1
            and len(message.text) > 1
            and len(message.text) < 21
        ):
            await message.answer(text=f"Принято ваше имя: {message.text}.")
            cmd_10 = f"INSERT INTO login(tg_id, first_name, second_name, gmail, phone_number, money, kripto) VALUES ({message.chat.id}, '{message.text}', '', '', '', 10000, 0);"
            db.cursor.execute(cmd_10)
            db.conn.commit()
            await message.answer(
                text="Введите свою фамилию. \nФамилия может содержать только буквы! \nМинимальное количество символов 4, максимальное 10: "
            )
            await botst.await_second.set()
        else:
            await message.answer(text="Прочитайте правило и введите снова!")
            await botst.await_first.set()
    else:
        await message.answer(text="Прочитайте правило и введите снова!")


@dp.message_handler(state=botst.await_second)
async def reqistr2(message: Message):
    if message.text:
        if message.text.isalpha() and len(message.text) > 3 and len(message.text) < 11:
            await message.answer(text=f"Принято ваша фамилия: {message.text}.")
            cmd_7 = f"UPDATE login SET second_name = '{message.text}' WHERE tg_id = {message.chat.id};"
            db.cursor.execute(cmd_7)
            db.conn.commit()
            await message.answer(
                text="Введите свою эллектронную почту: \nПример: example@gmail.com"
            )
            await botst.await_third.set()
        else:
            await message.answer(text="Прочитайте правило и введите снова!")
            await botst.await_second.set()
    else:
        await message.answer(text="Прочитайте правило и введите снова!")
        await botst.await_second.set()


@dp.message_handler(state=botst.await_third)
async def reqistr3(message: Message):
    if message.text:
        chat_id = message.chat.id
        cmd_22 = f"INSERT INTO attempts(message_id) VALUES ({message.chat.id});"
        db.cursor.execute(cmd_22)
        db.conn.commit()
        addressToVerify = message.text.lower()
        match = re.match(
            "^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$",
            addressToVerify,
        )

        records = dns.resolver.query("scottbrady91.com", "MX")
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)

        # Получает имя хоста локального сервера!
        host = socket.gethostname()

        # Настройка SMTP
        server = smtplib.SMTP()
        server.set_debuglevel(0)

        # SMTP разговор
        server.connect(mxRecord)
        server.helo(host)
        server.mail("me@domain.com")
        code, message = server.rcpt(str(addressToVerify))
        server.quit()
        if code == 250:
            cmd_17 = (
                f"UPDATE login SET gmail = '{addressToVerify}' WHERE tg_id = {chat_id};"
            )
            db.cursor.execute(cmd_17)
            db.conn.commit()
            # Создать экземпляр объекта сообщения
            msg = MIMEMultipart()
            random_code = random.randrange(100000, 999999)
            cmd_29 = f"INSERT INTO code(doc, tag_id) VALUES ({random_code}, {chat_id});"
            db.cursor.execute(cmd_29)
            db.conn.commit()
            message = f"Проверочный код: {random_code}"

            # Настройка параметров сообщения
            password = "" # Email password
            msg["From"] = "" # Your email
            msg["To"] = f"{addressToVerify}"
            msg["Subject"] = "Финансовая биржa!"

            # Добавить сообщение
            msg.attach(MIMEText(message, "plain"))

            # Создать сервер
            server = smtplib.SMTP("smtp.gmail.com: 587")

            server.starttls()

            # Учетные данные для входа в систему и для отправки почты
            server.login(msg["From"], password)

            # Отправка сообщения через сервер
            global time1
            server.sendmail(msg["From"], msg["To"], msg.as_string())
            server.quit()
            await bot.send_message(
                chat_id=chat_id,
                text=f'Введите 6-значный код. \nКод был отправлен на почту: {addressToVerify} \nЕсли вам не пришо сообщение, то провертье ярлык "Спам"',
            )
            time1 = time.time()
            await botst.await_four.set()
        else:
            await bot.send_message(
                chat_id=chat_id, text="Было неправильно введена эллектронная почта!"
            )
            await botst.await_third.set()
    else:
        await message.answer(text="Прочитайте правило и введите снова!")


@dp.message_handler(state=botst.await_four)
async def reqistr4(message: Message):
    if message.text:
        cmd_011 = f"SELECT doc FROM code WHERE tag_id = {message.from_user.id}"
        db.cursor.execute(cmd_011)
        ran_code = db.cursor.fetchall()
        time2 = time.time()
        if time2 - time1 > 300:
            await message.answer(text="Время вышло. \nНачните регистрацию заново!")
            cmd_08 = f"DELETE FROM login WHERE tg_id = {message.from_user.id};"
            db.cursor.execute(cmd_08)
            cmd_21d = f"DELETE FROM attempts WHERE message_id = {message.from_user.id};"
            db.cursor.execute(cmd_21d)
            db.conn.commit()
            await botst.await_first.set()
        elif message.text == str(ran_code[-1][0]):
            await message.answer(
                text="Вы почти у цели . . . \nНажмите, чтобы отправить номер телефона.",
                reply_markup=buttons.Number().number(),
            )
            cmd_21 = f"DELETE FROM attempts WHERE message_id = {message.from_user.id};"
            db.cursor.execute(cmd_21)
            db.conn.commit()
            await botst.await_five.set()
        else:
            cmd_0 = (
                f"SELECT att FROM attempts WHERE message_id = {message.from_user.id}"
            )
            db.cursor.execute(cmd_0)
            attempts = db.cursor.fetchone()
            await message.answer(
                text=f"Вы ввели неверный код! \nПопытки {attempts[0]}!"
            )

            if attempts[0] == 3:
                cmd_1 = f"UPDATE attempts SET att = 2 WHERE message_id = {message.from_user.id}"
                db.cursor.execute(cmd_1)
                db.conn.commit()
            elif attempts[0] == 2:
                cmd_3 = f"UPDATE attempts SET att = 1 WHERE message_id = {message.from_user.id}"
                db.cursor.execute(cmd_3)
                db.conn.commit()
            elif attempts[0] == 1:
                cmd_4 = f"UPDATE attempts SET att = 0 WHERE message_id = {message.from_user.id}"
                db.cursor.execute(cmd_4)
                db.conn.commit()
            else:
                cmd_00 = (
                    f"DELETE FROM attempts WHERE message_id = {message.from_user.id};"
                )
                db.cursor.execute(cmd_00)
                cmd_09 = f"DELETE FROM login WHERE tg_id = {message.from_user.id};"
                db.cursor.execute(cmd_09)
                db.conn.commit()
                await message.answer(text="Начните регистрацию заново!")
                await botst.await_first.set()
    else:
        await message.answer(text="Прочитайте правило и введите снова!")


@dp.message_handler(content_types=["contact"], state=botst.await_five)
async def phone_number(message: Message):
    if message.contact:
        cmd_9 = f"UPDATE login set phone_number = '{message.contact.phone_number}' WHERE tg_id = {message.chat.id};"
        db.cursor.execute(cmd_9)
        db.conn.commit()
        await message.answer(
            text="Мы успешно получили ваш номер телефона. \nВы можете пользоваться биржой!",
            reply_markup=buttons.Log().osnov(),
        )
        await botst.await_six.set()
    else:
        await message.answer(text="Прочитайте правило и введите снова!")


@dp.callback_query_handler(state=botst.await_six)
async def doktor_call(call: CallbackQuery):
    if call.data == "buy":
        await bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None,
        )
        await bot.send_message(
            chat_id=call.message.chat.id, text="Сколько вы хотите купить?"
        )
        await botst.await_seven.set()
    elif call.data == "sell":
        await bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None,
        )
        await bot.send_message(
            chat_id=call.message.chat.id, text="Сколько вы хотите продать?"
        )
        await botst.await_nine.set()
    elif call.data == "see":
        await bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None,
        )
        cmd_ldld = f"SELECT buying, trata, kurs FROM tran WHERE tg_id = {call.message.chat.id};"
        db.cursor.execute(cmd_ldld)
        tran = db.cursor.fetchall()
        cmd_ldld = (
            f"SELECT sell, prybyl, kurs FROM prod WHERE tg_id = {call.message.chat.id};"
        )
        db.cursor.execute(cmd_ldld)
        pryb = db.cursor.fetchall()

        for trn in tran:
            await bot.send_message(
                chat_id=call.message.chat.id,
                text=f"Купленные крипты: {trn[0]} \nСколько стоило: {trn[1]} \nПо какому курсу: {trn[2]}",
            )
        for prb in pryb:
            await bot.send_message(
                chat_id=call.message.chat.id,
                text=f"Проданной крипты: {prb[0]} \nСколько стоило: {prb[1]} \nПо какому курсу: {prb[2]}",
            )
        await bot.send_message(
            chat_id=call.message.chat.id,
            text="Вы вернулись в главное меню!",
            reply_markup=buttons.Log().osnov(),
        )
    elif call.data == "remove":
        await bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None,
        )
        await bot.send_message(
            chat_id=call.message.chat.id, text="Подтвердите личность."
        )
        msg = MIMEMultipart()
        random_code = random.randrange(100000, 999999)
        cmd_0gg = f"INSERT INTO code(doc, tag_id) VALUES ({random_code}, {call.message.chat.id});"
        db.cursor.execute(cmd_0gg)
        db.conn.commit()
        message1 = f"Проверочный код: {random_code}"

        cmd_ldld = f"SELECT gmail FROM login WHERE tg_id = {call.message.chat.id};"
        db.cursor.execute(cmd_ldld)
        gma = db.cursor.fetchone()
        # Настройка параметров сообщения
        password = "" # Email password
        msg["From"] = "" # Your email
        msg["To"] = f"{gma[0]}"
        msg["Subject"] = "Финансовая биржa!"

        # Добавить сообщение
        msg.attach(MIMEText(message1, "plain"))

        # Создать сервер
        server = smtplib.SMTP("smtp.gmail.com: 587")

        server.starttls()

        # Учетные данные для входа в систему и для отправки почты
        server.login(msg["From"], password)

        # Отправка сообщения через сервер
        global time3
        server.sendmail(msg["From"], msg["To"], msg.as_string())
        server.quit()
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=f'Введите 6-значный код. \nКод был отправлен на почту: {gma[0]} \nЕсли вам не пришло сообщение, то провертье ярлык "Спам" \nВам дается 5 минут!',
        )
        time3 = time.time()
        await botst.await_elev.set()
    elif call.data == "view":
        await bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None,
        )
        cmd_dd = f"SELECT val FROM currency;"
        db.cursor.execute(cmd_dd)
        kurs = db.cursor.fetchone()
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=kurs[0],
            reply_markup=buttons.Log().osnov(),
        )
    elif call.data == "bal":
        await bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None,
        )
        cmd_ddr = f"SELECT money FROM login WHERE tg_id = {call.message.chat.id};"
        db.cursor.execute(cmd_ddr)
        money = db.cursor.fetchone()
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=f"Ваш баланс: {money[0]}",
            reply_markup=buttons.Log().osnov(),
        )
    elif call.data == "krip":
        await bot.edit_message_reply_markup(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=None,
        )
        cmd_ssd = f"SELECT kripto FROM login WHERE tg_id = {call.message.chat.id};"
        db.cursor.execute(cmd_ssd)
        kripta = db.cursor.fetchone()
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=f"Ваша крипта: {kripta[0]}",
            reply_markup=buttons.Log().osnov(),
        )


@dp.message_handler(state=botst.await_seven)
async def get_ask_kript(message: Message):
    if message.text:
        try:
            money = float(message.text)
            cmd_90 = f"SELECT b_kripto FROM birzha;"
            db.cursor.execute(cmd_90)
            krip = db.cursor.fetchone()

            cmd_kk = f"SELECT money FROM login WHERE tg_id = {message.from_user.id};"
            db.cursor.execute(cmd_kk)
            mon = db.cursor.fetchone()

            cmd_l9 = f"SELECT val FROM currency;"
            db.cursor.execute(cmd_l9)
            curs = db.cursor.fetchone()
            if 0 < money <= krip[0] and money * curs[0] <= mon[0]:
                cmd_2p = f"INSERT INTO wait(message_id, skolko) VALUES ({message.chat.id}, {money});"
                db.cursor.execute(cmd_2p)
                db.conn.commit()
                await message.answer(text="Подтвердите личность!")
                # Создать экземпляр объекта сообщения
                msg = MIMEMultipart()
                random_code = random.randrange(100000, 999999)
                cmd_2o = f"INSERT INTO code(doc, tag_id) VALUES ({random_code}, {message.chat.id});"
                db.cursor.execute(cmd_2o)
                db.conn.commit()
                message1 = f"Проверочный код: {random_code}"

                cmd_909 = f"SELECT gmail FROM login WHERE tg_id = {message.chat.id};"
                db.cursor.execute(cmd_909)
                gma = db.cursor.fetchone()
                # Настройка параметров сообщения
                password = "" # Email password
                msg["From"] = "" # Your email
                msg["To"] = f"{gma[0]}"
                msg["Subject"] = "Финансовая биржa!"

                # Добавить сообщение
                msg.attach(MIMEText(message1, "plain"))

                # Создать сервер
                server = smtplib.SMTP("smtp.gmail.com: 587")

                server.starttls()

                # Учетные данные для входа в систему и для отправки почты
                server.login(msg["From"], password)

                # Отправка сообщения через сервер
                global time3
                server.sendmail(msg["From"], msg["To"], msg.as_string())
                server.quit()
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f'Введите 6-значный код. \nКод был отправлен на почту: {gma[0]} \nЕсли вам не пришло сообщение, то провертье ярлык "Спам" \nВам дается 5 минут!',
                )
                time3 = time.time()
                await botst.await_eight.set()
            else:
                await bot.send_message(
                    chat_id=message.from_user.id,
                    text="У вас недостаточно денег на балансе!",
                    reply_markup=buttons.Log().osnov(),
                )
        except ValueError:
            await bot.send_message(chat_id=message.chat.id, text="Только цифры!")
    else:
        await message.answer(text="Прочитайте правило и введите снова!")


@dp.message_handler(state=botst.await_eight)
async def check(message: Message):
    cmd_011 = f"SELECT doc FROM code WHERE tag_id = {message.from_user.id}"
    db.cursor.execute(cmd_011)
    ran_code = db.cursor.fetchall()
    time4 = time.time()
    if time4 - time3 > 300:
        await message.answer(
            text="Время вышло. \nВы вышли в меню!", reply_markup=buttons.Log().osnov()
        )
        await botst.await_six.set()
    elif message.text == str(ran_code[-1][0]):
        cmd_99 = f"SELECT skolko FROM wait WHERE message_id = {message.from_user.id};"
        db.cursor.execute(cmd_99)
        krip = db.cursor.fetchall()
        amount = krip[-1][0]

        cmd_l9 = f"SELECT val FROM currency;"
        db.cursor.execute(cmd_l9)
        curs = db.cursor.fetchone()
        equels = amount * curs[0]

        cmd_499 = f"UPDATE login SET money = money-{equels} WHERE tg_id = {message.from_user.id};"
        db.cursor.execute(cmd_499)

        cmd_00 = f"UPDATE login SET kripto = kripto+{amount} WHERE tg_id = {message.from_user.id};"
        db.cursor.execute(cmd_00)

        cmd_34 = f"UPDATE birzha SET b_money = b_money+{equels};"
        db.cursor.execute(cmd_34)

        cmd_00 = f"UPDATE birzha SET b_kripto = b_kripto-{amount};"
        db.cursor.execute(cmd_00)

        cmd_2opp = f"INSERT INTO tran(buying, trata, kurs, tg_id) VALUES ({amount}, {equels}, {curs[0]}, {message.from_user.id});"
        db.cursor.execute(cmd_2opp)
        db.conn.commit()

        await message.answer(
            text="Вы прошли подтверждение! \nВалюта успешно куплена!",
            reply_markup=buttons.Log().osnov(),
        )
        await botst.await_six.set()
    else:
        await message.answer(text="Код введен неправильно! \nПопробуйте еще раз!")


# ----------------------------------
@dp.message_handler(state=botst.await_nine)
async def get_ask_kript5(message: Message):
    if message.text:
        try:
            kripta = float(message.text)
            cmd_90 = f"SELECT b_money FROM birzha;"
            db.cursor.execute(cmd_90)
            krip = db.cursor.fetchone()

            cmd_kk = f"SELECT kripto FROM login WHERE tg_id = {message.from_user.id};"
            db.cursor.execute(cmd_kk)
            mon = db.cursor.fetchone()

            cmd_l9 = f"SELECT val FROM currency;"
            db.cursor.execute(cmd_l9)
            curs = db.cursor.fetchone()
            if 0 < kripta <= mon[0] and kripta * curs[0] <= krip[0]:
                cmd_2p = f"INSERT INTO wait(message_id, skolko) VALUES ({message.chat.id}, {kripta});"
                db.cursor.execute(cmd_2p)
                db.conn.commit()
                await message.answer(text="Подтвердите личность!")
                # Создать экземпляр объекта сообщения
                msg = MIMEMultipart()
                random_code = random.randrange(100000, 999999)
                cmd_2o = f"INSERT INTO code(doc, tag_id) VALUES ({random_code}, {message.chat.id});"
                db.cursor.execute(cmd_2o)
                db.conn.commit()
                message1 = f"Проверочный код: {random_code}"

                cmd_909 = f"SELECT gmail FROM login WHERE tg_id = {message.chat.id};"
                db.cursor.execute(cmd_909)
                gma = db.cursor.fetchone()
                # Настройка параметров сообщения
                password = "05052005bek"
                msg["From"] = "bigcompany141@gmail.com"
                msg["To"] = f"{gma[0]}"
                msg["Subject"] = "Финансовая биржa!"

                # Добавить сообщение
                msg.attach(MIMEText(message1, "plain"))

                # Создать сервер
                server = smtplib.SMTP("smtp.gmail.com: 587")

                server.starttls()

                # Учетные данные для входа в систему и для отправки почты
                server.login(msg["From"], password)

                # Отправка сообщения через сервер
                global time3
                server.sendmail(msg["From"], msg["To"], msg.as_string())
                server.quit()
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f'Введите 6-значный код. \nКод был отправлен на почту: {gma[0]} \nЕсли вам не пришло сообщение, то провертье ярлык "Спам" \nВам дается 5 минут!',
                )
                time3 = time.time()
                await botst.await_ten.set()
            else:
                await bot.send_message(
                    chat_id=message.from_user.id,
                    text="У вас недостаточно крипты!",
                    reply_markup=buttons.Log().osnov(),
                )
        except ValueError:
            await bot.send_message(chat_id=message.chat.id, text="Только цифры!")
    else:
        await message.answer(text="Прочитайте правило и введите снова!")


@dp.message_handler(state=botst.await_ten)
async def check5(message: Message):
    if message.text:
        cmd_011 = f"SELECT doc FROM code WHERE tag_id = {message.from_user.id}"
        db.cursor.execute(cmd_011)
        ran_code = db.cursor.fetchall()
        time4 = time.time()
        if time4 - time3 > 300:
            await message.answer(
                text="Время вышло. \nВы вышли в меню!",
                reply_markup=buttons.Log().osnov(),
            )
            await botst.await_six.set()
        elif message.text == str(ran_code[-1][0]):
            cmd_99 = (
                f"SELECT skolko FROM wait WHERE message_id = {message.from_user.id};"
            )
            db.cursor.execute(cmd_99)
            krip = db.cursor.fetchall()
            amount = krip[-1][0]

            cmd_l9 = f"SELECT val FROM currency;"
            db.cursor.execute(cmd_l9)
            curs = db.cursor.fetchone()
            equels = amount * curs[0]

            cmd_499 = f"UPDATE login SET money = money+{equels} WHERE tg_id = {message.from_user.id};"
            db.cursor.execute(cmd_499)

            cmd_00 = f"UPDATE login SET kripto = kripto-{amount} WHERE tg_id = {message.from_user.id};"
            db.cursor.execute(cmd_00)

            cmd_34 = f"UPDATE birzha SET b_money = b_money-{equels};"
            db.cursor.execute(cmd_34)

            cmd_00 = f"UPDATE birzha SET b_kripto = b_kripto+{amount};"
            db.cursor.execute(cmd_00)

            cmd_2opp = f"INSERT INTO prod(sell, prybyl, kurs, tg_id) VALUES ({amount}, {equels}, {curs[0]}, {message.from_user.id});"
            db.cursor.execute(cmd_2opp)
            db.conn.commit()

            await message.answer(
                text="Вы прошли подтверждение! \nВалюта успешно продана!",
                reply_markup=buttons.Log().osnov(),
            )
            await botst.await_six.set()
        else:
            await message.answer(text="Код введен неправильно! \nПопробуйте еще раз!")
    else:
        await message.answer(text="Прочитайте правило и введите снова!")


# ----------------------------------------
@dp.message_handler(state=botst.await_elev)
async def check3(message: Message):
    cmd_011 = f"SELECT doc FROM code WHERE tag_id = {message.from_user.id}"
    db.cursor.execute(cmd_011)
    ran_code = db.cursor.fetchall()
    time4 = time.time()
    if time4 - time3 > 300:
        await message.answer(
            text="Время вышло. \nВы вышли в меню!", reply_markup=buttons.Log().osnov()
        )
        await botst.await_six.set()
    elif message.text == str(ran_code[-1][0]):
        cmd_777 = f"SELECT money FROM login WHERE tg_id ={message.from_user.id};"
        db.cursor.execute(cmd_777)
        monn = db.cursor.fetchone()

        cmd_712 = f"SELECT kripto FROM login WHERE tg_id = {message.from_user.id};"
        db.cursor.execute(cmd_712)
        krript = db.cursor.fetchone()

        cmd_3499 = f"UPDATE birzha SET b_money = b_money+{monn[0]};"
        db.cursor.execute(cmd_3499)

        cmd_666 = f"UPDATE birzha SET b_kripto = b_kripto+{krript[0]};"
        db.cursor.execute(cmd_666)

        cmd_201 = f"DELETE FROM login WHERE tg_id = {message.from_user.id};"
        db.cursor.execute(cmd_201)
        db.conn.commit()

        await message.answer(
            text="Вы прошли подтверждение! \nАккаунт успешно удален! \nМожете пройти регистрацию снова."
        )
        await botst.await_first.set()
    else:
        await message.answer(text="Код введен неправильно! \nПопробуйте еще раз!")


if __name__ == "__main__":
    program1 = multiprocessing.Process(target=executor.start_polling, args=(dp,))
    program2 = multiprocessing.Process(target=db.valut)
    program1.start()
    program2.start()
