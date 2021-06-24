from types import SimpleNamespace
import psycopg2
import os 
import json
from bs4 import BeautifulSoup
import pathlib

PATH = pathlib.Path(__file__).parent.parent

dbname = input("Your database name: ")
dbuser = input("Your database user: ")
dbpswd = input("Your database password: ")

conn = psycopg2.connect(
    dbname=dbname, 
    user=dbuser, 
    password=dbpswd, 
    host='localhost')
cursor = conn.cursor()

#-----------------------------------------------------------------------------------------------

class Scraper_main:
    def main(self):
        links = [f'{PATH}/mypizza.kg/Menu/Category/4354.html', f'{PATH}/mypizza.kg/Menu/Category/4372.html', f'{PATH}/mypizza.kg/Menu/Category/4365.html', f'{PATH}/mypizza.kg/Menu/Category/4358.html', f'{PATH}/mypizza.kg/Menu/Category/4356.html']
        paths = [f'{PATH}/imperia/menu_img/breakfast', f'{PATH}/imperia/menu_img/pizza_40_cm', f'{PATH}/imperia/menu_img/rolls', f'{PATH}/imperia/menu_img/salads', f'{PATH}/imperia/menu_img/snacks']
        all_menu = []
        for ind in range(len(links)):
            list_1 = []
            list_2 = []
            list_3 = []
            url = open(links[ind])
            page_soup_html = BeautifulSoup(url, 'html.parser')
            blocks = page_soup_html.find_all('script', type="text/javascript")
            peremen = 'categoryController.init'
            peremen2 = '});'
            ht = blocks[4].__str__()
            peremen3 = ht.find(peremen)+24
            peremen4 = ht.find(peremen2)-194
            osnova = json.loads(ht[peremen3:peremen4])
            for dic in osnova:
                list_1.append(dic.get('Name'))
                list_2.append(dic.get('Price'))
                pochty_img = dic.get('PicturePath')
                img_link = str(pochty_img).replace(' ', '%20').replace('\\', '/')
                op = str(pochty_img).replace('jpg/2021\\', 'jpg/').replace('Острые пиццы\\','').split('jpg/')
                list_3.append(op[1])
                img = os.system(f'wget -c {img_link} -P {paths[ind]}')
            all_menu.append([list_1, list_2, list_3])
        return all_menu

def zapusk1(arg1):
    menu_func = arg1.main()
    tables = ['breakfast', 'pizza_40_cm', 'rolls', 'salads', 'snacks']
    for index in range(len(tables)):
        cmd = f'SELECT table_name FROM information_schema.tables WHERE table_name = \'{tables[index]}\';'
        print(cmd)
        cursor.execute(cmd)
        table_name = cursor.fetchone()
        try:
            if tables[index] == table_name[0]:
                cmd_0 = f'DROP TABLE {tables[index]};'
                cursor.execute(cmd_0)
                conn.commit()
        except TypeError:
            pass
        
        cmd_1 = f'''CREATE TABLE {tables[index]}(
            id SERIAL PRIMARY KEY, 
            names VARCHAR(80) NOT NULL, 
            images_path VARCHAR(80) NOT NULL, 
            prices VARCHAR(30) NOT NULL);'''
        cursor.execute(cmd_1)

        query1 = f'INSERT INTO {tables[index]}(names, images_path, prices) VALUES '
        for i in range(len(menu_func[index][0])):
            query1 += f'(\'{menu_func[index][0][i]}\', \'{menu_func[index][2][i]}\', \'{menu_func[index][1][i]}\'),'

        sql_query1 = query1[:-1] + ';'

        cursor.execute(sql_query1)
        conn.commit()

#-----------------------------------------------------------------------------------------------

class Shares:
    def shar(self):
        html_path = os.listdir(path=f'{PATH}/mypizza.kg/Shares/ShareItem')
        all_shares = []
        for html in html_path:
            header_op = []
            with open(f'{PATH}/mypizza.kg/Shares/ShareItem/{html}', 'r') as t:
                text_pochty = t.read()
            soup = BeautifulSoup(text_pochty, 'html.parser')
            texts = soup.find_all("p", attrs={"style": "white-space: pre-line"})
            titles = soup.find_all("title", attrs={"id": "Tname"})
            img_path = soup.find_all("img", attrs={"alt": ""})
            for title in titles:
                title1 = str(title.text).replace('\r', '')
                header_op.append(title1)
            for text in texts:
                text1 = str(text.text).replace('\r', '')
                header_op.append(text1)
            for path in img_path:
                path_img = path["src"]
                if 'http://mobile.mypizza.kg:9720/' in path_img:
                    pop = path_img
                    header_op.append(str(pop).replace('http://mobile.mypizza.kg:9720/VirtualCardSecureService.svc/',''))
                    os.system(f'wget -c {path_img} -P {PATH}/imperia/shares_img')
            osnova = []
            osnova = [i.replace('\n', '').replace('                                            ',' ') for i in header_op]
            all_shares.append(osnova)
        return all_shares

def zapusk2(arg2):
    shares_func = arg2.shar()

    cmd = f'SELECT table_name FROM information_schema.tables WHERE table_name = \'share\';'
    cursor.execute(cmd)
    table_name = cursor.fetchone()
    if 'share' == table_name[0]:
        cmd_0 = f'DROP TABLE share;'
        cursor.execute(cmd_0)
        conn.commit()

    cmd_1 = '''CREATE TABLE share(
        id SERIAL PRIMARY KEY, 
        headers VARCHAR(80) NOT NULL, 
        description TEXT NOT NULL,
        images VARCHAR(80) NOT NULL);'''
    cursor.execute(cmd_1)

    query2 = 'INSERT INTO share(headers, description, images) VALUES '
    for i in range(len(shares_func)):
        query2 += f'(\'{shares_func[i][0]}\', \'{shares_func[i][1]}\', \'{shares_func[i][2]}\'),'

    sql_query2 = query2[:-1] + ';'

    cursor.execute(sql_query2)
    conn.commit()   

#-----------------------------------------------------------------------------------------------

class Company:
    def comp(self):
        html_path = os.listdir(path=f'{PATH}/mypizza.kg/Company')
        all_amout_company = []
        for html in html_path:
            header_op = []
            with open(f'{PATH}/mypizza.kg/Company/{html}', 'r') as t:
                text_pochty = t.read()
            soup = BeautifulSoup(text_pochty, 'html.parser')
            texts = soup.find_all("p", attrs={"style": "white-space: pre-line"})
            titles = soup.find_all("title", attrs={"id": "Tname"})
            texts2 = soup.find_all("div", attrs={"class": "c-content__text"})
            for title in titles:
                title1 = str(title.text).replace('\r', '')
                header_op.append(title1)
                for text2 in texts2:
                    text3 = str(text2.text).replace('\r', '')
                    header_op.append(text3)
            osnova = []
            osnova = [i.replace('\n', '').replace('•\t','').replace('                                ','').replace('                                        ',' ').replace('                                    ',' ') for i in header_op]

            all_amout_company.append(osnova)
        return all_amout_company

def zapusk3(arg3):
    company_func = arg3.comp()

    cmd = "SELECT table_name FROM information_schema.tables WHERE table_name = 'company';"
    cursor.execute(cmd)
    table_name = cursor.fetchone()
    try:
        if 'company' in table_name[0]:
            cmd_0 = f'DROP TABLE company;'
            cursor.execute(cmd_0)
            conn.commit()
    except TypeError:
        pass

    cmd_1 = '''CREATE TABLE company(
        id SERIAL PRIMARY KEY, 
        headers VARCHAR(80) NOT NULL, 
        description TEXT NOT NULL);'''
    cursor.execute(cmd_1)

    query3 = 'INSERT INTO company(headers, description) VALUES '
    for i in range(len(company_func)):
        try:
            query3 += f'(\'{company_func[i][0]}\', \'{company_func[i][1]}\'),'
        except IndexError:
            query3 += f'(\'{company_func[i][0]}\', \'В разработке\'),'


    sql_query3 = query3[:-1] + ';'

    cursor.execute(sql_query3)
    conn.commit()   

#-----------------------------------------------------------------------------------------------

class Vacancies:
    def vacan(self):
        login = os.getlogin()
        html_path = os.listdir(path=f'{PATH}/mypizza.kg/Vacancies/VacancyItem')
        all_vacancies = []
        with open(f'{PATH}/mypizza.kg/Vacancies.html', 'r') as te:
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
            with open(f'{PATH}/mypizza.kg/Vacancies/VacancyItem/{html}', 'r') as t:
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
            osnova = [i.replace('\n', '').replace('         ','').replace('                        ',' ').replace('                                        ',' ').replace('                                    ','') for i in main]
            all_vacancies.append(osnova)
        return all_vacancies

def zapusk4(arg4):
    vacancies_func = arg4.vacan()

    cmd = 'SELECT table_name FROM information_schema.tables WHERE table_name = \'vacancies\';'
    cursor.execute(cmd)
    table_name = cursor.fetchone()
    if 'vacancies' in table_name[0]:
        cmd_0 = f'DROP TABLE vacancies;'
        cursor.execute(cmd_0)
        conn.commit()

    cmd_1 = '''CREATE TABLE vacancies(
        id SERIAL PRIMARY KEY, 
        headers VARCHAR(80) NOT NULL, 
        description TEXT NOT NULL);'''
    cursor.execute(cmd_1)

    query4 = 'INSERT INTO vacancies(headers, description) VALUES '
    for i in range(len(vacancies_func)):
        query4 += f'(\'{vacancies_func[i][0]}\', \'{vacancies_func[i][1]}\'),'

    sql_query4 = query4[:-1] + ';'

    cursor.execute(sql_query4)
    conn.commit()   

