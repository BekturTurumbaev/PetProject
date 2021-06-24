import time
import random
import psycopg2


dbname = input("Your database name: ")
dbuser = input("Your database user: ")
dbpswd = input("Your database password: ")

connection = psycopg2.connect(
    dbname=dbname, user=dbuser, password=dbpswd, host="localhost"
)
cursor = connection.cursor()


def valut():
    conn2 = psycopg2.connect(
        dbname=dbname, user=dbuser, password=dbpswd, host="localhost"
    )
    cursor = conn2.cursor()

    while True:
        time.sleep(10)
        valuta = round(random.uniform(80.00, 90.00), 2)
        upd = f"UPDATE currency SET val = {valuta};"
        cursor.execute(upd)
        conn2.commit()

# Create all tables
# tables = ["CREATE TABLE attempts(message_id INT, att INT DEFAULT 3);","CREATE TABLE code(doc INT, tag_id INT);","CREATE TABLE wait(message_id INT, skolko INT);","CREATE TABLE birzha(b_money INT DEFAULT 0, b_kripto INT DEFAULT 15000);","CREATE TABLE tran(buying INT, trata INT, kurs INT, tg_id INT);","CREATE TABLE prod(sell INT, prybyl INT, kurs INT, tg_id INT);","CREATE TABLE currency(val FLOAT DEFAULT 83.01);","CREATE TABLE login(id SERIAL PRIMARY KEY,tg_id INT NOT NULL,first_name VARCHAR(22) NOT NULL,second_name VARCHAR(20) NOT NULL,gmail VARCHAR(40) NOT NULL,phone_number VARCHAR(20) NOT NULL,money INT NOT NULL,kripto INT NOT NULL);"]
# for table in tables:
#     cursor.execute(table)
# connection.commit()

# Drop all tables
# drop_tables = ['DROP TABLE attempts;','DROP TABLE code;','DROP TABLE wait;','DROP TABLE birzha;','DROP TABLE tran;','DROP TABLE prod;','DROP TABLE currency;','DROP TABLE login;']
# for drop in drop_tables:
#     cursor.execute(drop)
# connection.commit()