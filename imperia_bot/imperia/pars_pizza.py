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
            shutil.rmtree(paths[ind])
            url = open(links[ind])
            page_soup_html = BeautifulSoup(url, 'html.parser')
            blocks = page_soup_html.find_all('script', type="text/javascript")
            peremen = 'categoryController.init'
            peremen2 = '});'
            img_path = []
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
                op = str(pochty_img).replace('jpg/2021\\', 'jpg/').replace('Острые пиццы\\','').split('jpg/')
                img_path.append(op[1])
                img = os.system(f'wget {img_link} -P {paths[ind]}')
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
