import psycopg2
import os 
import json
from bs4 import BeautifulSoup

class Vacancies:
    def vacan(self):
        html_path = os.listdir(path='/home/asus/Desktop/mypizza.kg/Vacancies/VacancyItem')
        all_vacancies = []
        with open('/home/asus/Desktop/mypizza.kg/Vacancies.html', 'r') as te:
            text_pochty_os = te.read()
        soup = BeautifulSoup(text_pochty_os, 'html.parser')
        texts2 = soup.find_all("p", attrs={"style": "white-space: pre-line"})
        titles1 = soup.find_all("h1", attrs={"class": "c-main__title"})
        nachalo = []
        for title in titles1:
            nachalo.append(title.text)
            for txt in texts2:
                nachalo.append(txt.text)
            perho = []
            perho = [i.replace('\n', '').replace('                                   ','').replace('                                ','') for i in nachalo]
            all_vacancies.append(perho)
        for html in html_path:
            main = []
            with open(f'/home/asus/Desktop/mypizza.kg/Vacancies/VacancyItem/{html}', 'r') as t:
                text_pochty = t.read()
            soup = BeautifulSoup(text_pochty, 'html.parser')
            texts = soup.find_all("div", attrs={"style": "white-space: pre-line"})
            titles = soup.find_all("div", attrs={"class": "c-vacancy__title"})
            for title in titles:
                title1 = str(title.text).replace('\r', '')
                main.append(title1)
                for text in texts:
                    text1 = str(text.text).replace('\r', '')
                    main.append(text1)
            osnova = []
            osnova = [i.replace('\n', '').replace('                                        ',' ').replace('                                    ','') for i in main]
            all_vacancies.append(osnova)
        yield all_vacancies


vacancies = Vacancies()
vacancies_func = [share for share in vacancies.vacan()]

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
if 'vacancies' in drop:
    cmd_0 = f'DROP TABLE vacancies;'
    cursor.execute(cmd_0)
    conn.commit()

cmd_1 = '''CREATE TABLE vacancies(
    id SERIAL PRIMARY KEY, 
    headers VARCHAR(80) NOT NULL, 
    description TEXT NOT NULL);'''
cursor.execute(cmd_1)

query = 'INSERT INTO vacancies(headers, description) VALUES '
for i in range(len(vacancies_func[0])):
    query += f'(\'{vacancies_func[0][i][0]}\', \'{vacancies_func[0][i][1]}\'),'

sql_query = query[:-1] + ';'

cursor.execute(sql_query)
conn.commit()   

cursor.close()
conn.close()


