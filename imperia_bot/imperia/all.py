import psycopg2
import os 
import shutil
import json
from bs4 import BeautifulSoup

class Scraper:
    def main(self):
        links = ['/home/asus/Desktop/mypizza.kg/Menu/Category/4354.html', '/home/asus/Desktop/mypizza.kg/Menu/Category/4372.html', '/home/asus/Desktop/mypizza.kg/Menu/Category/4365.html', '/home/asus/Desktop/mypizza.kg/Menu/Category/4358.html', '/home/asus/Desktop/mypizza.kg/Menu/Category/4356.html']
        paths = ['/home/asus/Desktop/imperia/menu_img/breakfast', '/home/asus/Desktop/imperia/menu_img/pizza_40_cm', '/home/asus/Desktop/imperia/menu_img/rolls', '/home/asus/Desktop/imperia/menu_img/salads', '/home/asus/Desktop/imperia/menu_img/snacks']
        for ind in range(len(links)):
            try:
                shutil.rmtree(paths[ind])
            except FileNotFoundError:
                pass
            url = open(links[ind])
            page_soup_html = BeautifulSoup(url, 'html.parser')
            blocks = page_soup_html.find_all('script', type="text/javascript")
            peremen = 'categoryController.init'
            peremen2 = '});'
            names = []
            prices = []
            ht = blocks[4].__str__()
            peremen3 = ht.find(peremen)+24
            peremen4 = ht.find(peremen2)-194
            osnova = json.loads(ht[peremen3:peremen4])
            for dic in osnova:
                names.append(dic.get('Name'))
                prices.append(dic.get('Price'))
                pochty_img = dic.get('PicturePath')
                img_link = str(pochty_img).replace(' ', '%20').replace('\\', '/')
                img = os.system(f'wget {img_link} -P {paths[ind]}')
                img_path = os.listdir(path=paths[ind])
            yield names, img_path, prices

scraper = Scraper()

menu_func = [breakt for breakt in scraper.main()]


conn = psycopg2.connect(
    dbname='imperia', 
    user='postgres', 
    password='05052005', 
    host='localhost')
cursor = conn.cursor()

tables = ['breakfast', 'pizza_40_cm', 'rolls', 'salads', 'snacks']
for index in range(len(tables)):
    cmd = f'SELECT table_name FROM information_schema.tables;'
    cursor.execute(cmd)
    table_name = cursor.fetchall()
    drop = str(table_name).replace(',', '')
    if tables[index] in drop:
        cmd_0 = f'DROP TABLE {tables[index]};'
        cursor.execute(cmd_0)
        conn.commit()
    
    cmd_1 = f'''CREATE TABLE {tables[index]}(
        id SERIAL PRIMARY KEY, 
        names VARCHAR(80) NOT NULL, 
        images_path VARCHAR(80) NOT NULL, 
        prices VARCHAR(30) NOT NULL);'''
    cursor.execute(cmd_1)

    query = f'INSERT INTO {tables[index]}(names, images_path, prices) VALUES '
    for i in range(len(menu_func[index][0])):
        query += f'(\'{menu_func[index][0][i]}\', \'{menu_func[index][1][i]}\', \'{menu_func[index][2][i]}\'),'

    sql_query = query[:-1] + ';'

    cursor.execute(sql_query)
    conn.commit()

cursor.close()
conn.close()


class Shares:
    def shar(self):
        html_path = os.listdir(path='/home/asus/Desktop/mypizza.kg/Shares/ShareItem')
        all_shares = []
        for html in html_path:
            header_op = []
            with open(f'/home/asus/Desktop/mypizza.kg/Shares/ShareItem/{html}', 'r') as t:
                text_pochty = t.read()
            soup = BeautifulSoup(text_pochty, 'html.parser')
            texts = soup.find_all("p", attrs={"style": "white-space: pre-line"})
            titles = soup.find_all("title", attrs={"id": "Tname"})
            for title in titles:
                title1 = str(title.text).replace('\r', '')
                header_op.append(title1)
                for text in texts:
                    text1 = str(text.text).replace('\r', '')
                    header_op.append(text1)
            osnova = []
            osnova = [i.replace('\n', '').replace('                                            ','') for i in header_op]
            all_shares.append(osnova)
        yield all_shares


shares = Shares()
shares_func = [share for share in shares.shar()]
# print(shares_func[0][0][1])

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
if 'share' in drop:
    cmd_0 = f'DROP TABLE share;'
    cursor.execute(cmd_0)
    conn.commit()

cmd_1 = '''CREATE TABLE share(
    id SERIAL PRIMARY KEY, 
    headers VARCHAR(80) NOT NULL, 
    description TEXT NOT NULL);'''
cursor.execute(cmd_1)

query = 'INSERT INTO share(headers, description) VALUES '
for i in range(len(shares_func[0])):
    query += f'(\'{shares_func[0][i][0]}\', \'{shares_func[0][i][1]}\'),'

sql_query = query[:-1] + ';'

cursor.execute(sql_query)
conn.commit()   

cursor.close()
conn.close()


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
            osnova = [i.replace('\n', '').replace('                                        ','').replace('                                    ','') for i in main]
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
            osnova = [i.replace('\n', '').replace('•\t','').replace('                                        ','').replace('                                    ','') for i in header_op]
            all_shares.append(osnova)
        yield all_shares


company = Company()
company_func = [share for share in company.comp()]
# print(company_func[0])


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
