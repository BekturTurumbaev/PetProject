import time
import requests
import psycopg2
import os 
import csv
from bs4 import BeautifulSoup
from requests.api import head

op = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Referer": "https://www.redfin.com/",
    "Upgrade-Insecure-Requests": "1",
    "Content-Type": "text/plain;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Cookie": '''RF_CORVAIR_LAST_VERSION=368.0.0; RF_BROWSER_ID=uJN8rqjGRtqmOEz08L2_Qg; RF_BID_UPDATED=1; sortOrder=1; sortOption=special_blend; AKA_A2=A; AMP_TOKEN=%24NOT_FOUND; FEED_COUNT=0%3At; _uetsid=102ac700bdd911eb9e48ad579aa122bb; _uetvid=a21dd430b60411eba172e70ab6a3901d; _dc_gtm_UA-294985-1=1; audS=t'''
}
link = input("Введите ссылку сайта: ")

class Scraper:
    def __init__(self, url):
        main_html = self.get_html(url)
        self.soup = BeautifulSoup(main_html, 'html.parser')


    def get_html(self, url):
        # time.sleep(2.5.5)
        r = requests.get(url, headers = op)
        if r.status_code == 200:
            return r.text   
        elif r.status_code == 403:
            print('Вы заблокированы на этом сайте!')
            return 0
        elif r.status_code == 404:
            print('Страница не найдена!')
            return 0

        
    def main_link(self):
        path = os.path.dirname(os.path.abspath(__file__))
        dirc = 0
        i = 0
        try:
            os.mkdir(path + '/osnova')
        except FileExistsError:
            pass
        path2 = f'{path}/osnova'
        homes_price = []
        rest = []
        path_for_img = []
        time.sleep(2)
        picture_blocks = self.soup.find_all('div', class_='bottomV2')
        for block in picture_blocks:
            proverka_na_none = []
            list_price_ins = []
            loko = []
            try:
                os.mkdir(path2 + '/' + str(dirc))
            except FileExistsError:
                pass
            path3 = path2 + f'/{dirc}'
            path_for_img.append(path3)
            oson = block.a
            page_url = oson["href"]
            page_url = 'https://www.redfin.com' + page_url
            opa = self.get_html(page_url)
            page_soup_html = BeautifulSoup(opa, 'html.parser')
            # # Скачивание картин
            blocks_img = page_soup_html.find_all('img', class_ = 'landscape')
            name_img = page_soup_html.find_all('div', class_ = 'street-address')
            for img_block in blocks_img:
                img_link = img_block
                img_url = img_link["src"]
                img_file = requests.get(img_url).content
                # img_file = os.system('wget <ссылка> -P путь')
                for names in name_img:
                    name = names.span.text
                    with open(f'{path3}/{name}{i}.jpg', 'wb') as file:
                        file.write(img_file)
                    i+=1
                    print('Ready')
            dirc += 1
            # # Price Insights & Home Facts
            price_insights1 = page_soup_html.find_all('span', class_ = 'content text-right')
            text_home_price = page_soup_html.find_all('span', class_ = 'header font-color-gray-light inline-block') 
            for texts in text_home_price:
                p = texts.text
                proverka_na_none.append(p)
                for price in price_insights1:
                    price_text = price.text    
                    if 'List Price' in proverka_na_none:
                        list_price_ins.append(price_text)
                    else:
                        proverka_na_none.append(None)
                    if 'Price Sq.Ft' in proverka_na_none:
                        list_price_ins.append(price_text)
                    else:
                        proverka_na_none.append(None)
                    if 'Est. Mo. Payment' in proverka_na_none:
                        list_price_ins.append(price_text)
                    else:
                        proverka_na_none.append(None)
                    if 'Buyer' in proverka_na_none:
                        list_price_ins.append(price_text)
                    else:
                        proverka_na_none.append(None)
                    if 'Brokerage Compensation' in proverka_na_none:
                        list_price_ins.append(price_text)
                    else:
                        proverka_na_none.append(None)
                    if 'Redfin estimate' in proverka_na_none:
                        list_price_ins.append(price_text)
                    else:
                        proverka_na_none.append(None)
                    if 'HOA Dues' in proverka_na_none:
                        list_price_ins.append(price_text)
                    else:
                        proverka_na_none.append(None)
                    if 'Status' in proverka_na_none:
                        list_price_ins.append(price_text)
                    else:
                        proverka_na_none.append(None)
                    if 'Time on Redfin' in proverka_na_none:
                        list_price_ins.append(price_text)
                    else:
                        proverka_na_none.append(None)
                    if 'Property Type' in proverka_na_none:
                        list_price_ins.append(price_text)
                    else:
                        proverka_na_none.append(None)
                    if 'Year Built' in proverka_na_none:
                        list_price_ins.append(price_text)
                    else:
                        proverka_na_none.append(None)
                    if 'Style' in proverka_na_none:
                        list_price_ins.append(price_text)
                    else:
                        proverka_na_none.append(None)
                    if 'Community' in proverka_na_none:
                        list_price_ins.append(price_text)
                    else:
                        proverka_na_none.append(None)
                    if 'Lot Size' in proverka_na_none:
                        list_price_ins.append(price_text)
                    else:
                        proverka_na_none.append(None)
                    if 'MLS#' in proverka_na_none:
                        list_price_ins.append(price_text)
                    else:
                        proverka_na_none.append(None)
            homes_price.append(list_price_ins)  
            #all
            addres = page_soup_html.find_all('div', class_ = 'street-address')
            for addr in addres:
                ad = addr.span.text
                loko.append(ad)
            bed_bath = page_soup_html.find_all('div', class_ = 'statsValue')
            for mnogoe in bed_bath:
                prin = mnogoe.text
                loko.append(prin)
            areas = page_soup_html.find_all('span', class_ = 'statsValue')
            for area in areas:
                ar = area.text
                loko.append(ar)
            rest.append(loko)
        with open(f'{path}/All_information.csv', 'a') as csvfile:
            wr = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
            wr.writerow(['Price', 'Bedrooms', 'Bathrooms', 'Addres', 'Rest' ,'List Price', 'Price Sq.Ft', 'Est. Mo. Payment', 'Buyer', 'Brokerage Compensation', 'Redfin estimate', 'HOA Dues', 'Status', 'Time on Redfin', 'Property Type', 'Year Built', 'Style', 'Community', 'Lot Size', 'MLS#', 'path_for_img'])
        for i in range(len(homes_price)):
            wr.writerow([rest[i] + homes_price[i] + path_for_img])
        yield homes_price

def amount_of_pages():
    time.sleep(2.5)
    try:
        r = requests.get(link, headers = op)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            pagination = soup.find_all('a', class_='clickable goToPage')
            pages = []
            for block in pagination:
                span_block = block.text
                if span_block == '»':
                    pass
                else:
                    pages.append(int(span_block))
            
            return max(pages)
        else:
            return 'Hey bro, you lox)'
    except (requests.exceptions.ConnectionError, ValueError):
        print('Неправильно введен URL!')
    
# https://www.redfin.com/city/1826/MA/Boston
sa = []
try:
    try:
        for page in range(1, amount_of_pages()+1):
            html = f'{link}/page-{page}'
            scraper = Scraper(html)
            scraper.main_link()
            a = scraper.main_link()
            for i in a:
                sa.append(i)
    except (requests.ConnectionError):
            print('Ошибка соединение с сервером!')
except (TypeError):
    pass
# windscribe connect

if sa:
    bd_password = input("Введите пароль от Базы Данных: ")

    conn = psycopg2.connect(
        dbname='postgres', 
        user='postgres', 
        password=bd_password, 
        host='localhost'
    )

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE redfin(
        id SERIAL PRIMARY KEY, 
        List Price VARCHAR(30) NOT NULL, 
        Price Sq.Ft VARCHAR(30) NOT NULL, 
        Est. Mo. Payment VARCHAR(30) NOT NULL, 
        Buyer's Brokerage VARCHAR(30) NOT NULL, 
        Redfin estimate VARCHAR(30) NOT NULL,
        HOA Dues VARCHAR(30) NOT NULL,
        Home Facts VARCHAR(30) NOT NULL,
        Status VARCHAR(30) NOT NULL,
        Time on Redfin VARCHAR(30) NOT NULL,
        Property Type VARCHAR(30) NOT NULL,
        Year Built VARCHAR(30) NOT NULL,
        Style VARCHAR(30) NOT NULL,
        Community VARCHAR(30) NOT NULL,
        Lot Size VARCHAR(30) NOT NULL,
        Style VARCHAR(30) NOT NULL,
        MLS# VARCHAR(30) NOT NULL);'''
    )


    query = '''INSERT INTO freehtml5(List Price, Price Sq.Ft, Est. Mo. Payment, Buyer's Brokerage, Redfin estimate, HOA Dues, Home Facts, Status, Time on Redfin, Property Type, Year Built, Style, MLS#) VALUES '''

    for index in range(len(sa)):
        query += f'''(
    \'{a[index][index]}\',
    \'{a[index][index]}\',
    \'{a[index][index]}\', 
    \'{a[index][index]}\',
    \'{a[index][index]}\',
    \'{a[index][index]}\',
    \'{a[index][index]}\',
    \'{a[index][index]}\',
    \'{a[index][index]}\',
    \'{a[index][index]}\',
    \'{a[index][index]}\',
    \'{a[index][index]}\',
    \'{a[index][index]}\',
            
            ),'''

    sql_query = query[:-1] + ';'


    cursor.execute(sql_query)
    conn.commit()



    cursor.close()
    conn.close()
else:
    pass
