import psycopg2
import os 
import json
from bs4 import BeautifulSoup
from requests.api import head
# Оптимизарованная версия!
    # menu = ['/home/asus/Desktop/mypizza.kg/Menu/Category/4354.html', '/home/asus/Desktop/mypizza.kg/Menu/Category/4372.html', '/home/asus/Desktop/mypizza.kg/Menu/Category/4365.html', '/home/asus/Desktop/mypizza.kg/Menu/Category/4358.html', '/home/asus/Desktop/mypizza.kg/Menu/Category/4356.html']
    # for men in menu:
    #     pass

class Scraper:

    def breakfast(self):
        link = open('/home/asus/Desktop/mypizza.kg/Menu/Category/4354.html')
        page_soup_html = BeautifulSoup(link, 'html.parser')
        blocks = page_soup_html.find_all('script', type='text/javascript')
        peremen = 'categoryController.init'
        peremen2 = '});'
        path = '/home/asus/Desktop/imperia/menu_img/breakfast'
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
            img = os.system(f'wget {img_link} -P {path}')
            img_path = os.listdir(path=path)
        yield names, img_path, prices

    def pizza_40_cm(self):
        link = open('/home/asus/Desktop/mypizza.kg/Menu/Category/4372.html')
        page_soup_html = BeautifulSoup(link, 'html.parser')
        blocks = page_soup_html.find_all('script', type='text/javascript')
        peremen = 'categoryController.init'
        peremen2 = '});'
        path = '/home/asus/Desktop/imperia/menu_img/pizza_40_cm'
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
            img = os.system(f'wget {img_link} -P {path}')
            img_path = os.listdir(path=path)
        yield names, img_path, prices

    def rolls(self):
        link = open('/home/asus/Desktop/mypizza.kg/Menu/Category/4365.html')
        page_soup_html = BeautifulSoup(link, 'html.parser')
        blocks = page_soup_html.find_all('script', type='text/javascript')
        peremen = 'categoryController.init'
        peremen2 = '});'
        path = '/home/asus/Desktop/imperia/menu_img/rolls'
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
            img = os.system(f'wget {img_link} -P {path}')
            img_path = os.listdir(path=path)
        yield names, img_path, prices

    def salads(self):
        link = open('/home/asus/Desktop/mypizza.kg/Menu/Category/4358.html')
        page_soup_html = BeautifulSoup(link, 'html.parser')
        blocks = page_soup_html.find_all('script', type='text/javascript')
        peremen = 'categoryController.init'
        peremen2 = '});'
        path = '/home/asus/Desktop/imperia/menu_img/salads'
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
            img = os.system(f'wget {img_link} -P {path}')
            img_path = os.listdir(path=path)
        yield names, img_path, prices

    def snacks(self):
        link = open('/home/asus/Desktop/mypizza.kg/Menu/Category/4356.html')
        page_soup_html = BeautifulSoup(link, 'html.parser')
        blocks = page_soup_html.find_all('script', type='text/javascript')
        peremen = 'categoryController.init'
        peremen2 = '});'
        path = '/home/asus/Desktop/imperia/menu_img/snacks'
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
            img = os.system(f'wget {img_link} -P {path}')
            img_path = os.listdir(path=path)
        yield names, img_path, prices

scraper = Scraper()

func1 = [breakt for breakt in scraper.breakfast()]
func2 = [pizza for pizza in scraper.pizza_40_cm()]
func3 = [roll for roll in scraper.rolls()]
func4 = [salad for salad in scraper.salads()]
func5 = [snack for snack in scraper.snacks()]

conn = psycopg2.connect(
    dbname='imperia', 
    user='postgres', 
    password='05052005', 
    host='localhost')
cursor = conn.cursor()

tables = ['breakfast', 'pizza_40_cm', 'rolls', 'salads', 'snacks']
for table in tables:
    cursor.execute(f'''CREATE TABLE {table}(
        id SERIAL PRIMARY KEY, 
        names VARCHAR(80) NOT NULL, 
        images_path VARCHAR(80) NOT NULL, 
        prices VARCHAR(30) NOT NULL);''')

    query = f'INSERT INTO {table}(names, images_path, prices) VALUES '

    for index in range(len(func1[0[0]])):
        query += f'(\'{images[index]}\', \'{headers[index]}\', \'{dates[index]}\'),'

    sql_query = query[:-1] + ';'

    cursor.execute(sql_query)
    conn.commit()

cursor.close()
conn.close()