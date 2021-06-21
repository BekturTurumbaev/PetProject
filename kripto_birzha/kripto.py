import re

import dns.resolver

import socket
import smtplib

import random


addressToVerify ='turumbaevv@gmail.com'
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

records = dns.resolver.query('scottbrady91.com', 'MX')
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
server.mail('me@domain.com')
code, message = server.rcpt(str(addressToVerify))
server.quit()

# Предположим, 250 как успех
if code == 250:
    print('Success')
else:
    print('Bad')


#---------------------------------------------------------------------------

# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# Создать экземпляр объекта сообщения
msg = MIMEMultipart()
message = "Ну ты внатуре лох"
 
# Настройка параметров сообщения
password = "05052005bek"
msg['From'] = "bigcompany141@gmail.com"
msg['To'] = "turumbaevv@gmail.com"
msg['Subject'] = "Топ ха"
 
# Добавить сообщение
msg.attach(MIMEText(message, 'plain'))
 
# Создать сервер
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Учетные данные для входа в систему и для отправки почты
server.login(msg['From'], password)
 
 
# Отправка сообщения через сервер
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
 







# Во время регистрации бот спрашивает у пользователя следующие поля:
# Имя которое должно состоять только из букв
# Фамилия которая должна состоять только из букв
# РЕАЛЬНЫЙ email который нужно будет проверить

# Номер телефона которым пользователь ДОЛЖЕН ПОДЕЛИТЬСЯ

# Посмотреть курс валют

