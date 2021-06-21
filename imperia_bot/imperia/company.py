from re import I
import psycopg2
import os 
import json
from bs4 import BeautifulSoup

class Company:
    def comp(self):
        html_path = os.listdir(path='/home/asus/Desktop/mypizza.kg/Company')
        all_shares = []
        for html in html_path:
            header_op = []
            with open(f'/home/asus/Desktop/mypizza.kg/Company/{html}', 'r') as t:
                text_pochty = t.read()
            soup = BeautifulSoup(text_pochty, 'html.parser')
            texts = soup.find_all("p", attrs={"style": "white-space: pre-line"})
            titles = soup.find_all("title", attrs={"id": "Tname"})
            texts2 = soup.find_all("div", attrs={"class": "c-content__text"})
            for title in titles:
                title1 = str(title.text).replace('\r', '')
                header_op.append(title1)
                # for text in texts:
                #     text1 = str(text.text).replace('\r', '')
                #     header_op.append(text1)
                for text2 in texts2:
                    text3 = str(text2.text).replace('\r', '')
                    header_op.append(text3)
            osnova = []
            osnova = [i.replace('\n', '').replace('•\t','').replace('                                        ',' ').replace('                                    ','') for i in header_op]
            all_shares.append(osnova)
        yield all_shares


company = Company()
company_func = [share for share in company.comp()]


conn = psycopg2.connect(
    dbname='imperia', 
    user='postgres', 
    password='05052005', 
    host='localhost')
cursor = conn.cursor()

cmd = 'SELECT table_name FROM information_schema.tables;'
cursor.execute(cmd)
table_name = cursor.fetchall()
drop = str(table_name).replace(',', '')
if 'company' in drop:
    cmd_0 = f'DROP TABLE company;'
    cursor.execute(cmd_0)
    conn.commit()

cmd_1 = '''CREATE TABLE company(
    id SERIAL PRIMARY KEY, 
    headers VARCHAR(80) NOT NULL, 
    description TEXT NOT NULL);'''
cursor.execute(cmd_1)

query = 'INSERT INTO company(headers, description) VALUES '
for i in range(len(company_func[0])):
    try:
        query += f'(\'{company_func[0][i][0]}\', \'{company_func[0][i][1]}\'),'
    except IndexError:
        query += f'(\'{company_func[0][i][0]}\', \'В разработке\'),'


sql_query = query[:-1] + ';'

cursor.execute(sql_query)
conn.commit()   

cursor.close()
conn.close()
