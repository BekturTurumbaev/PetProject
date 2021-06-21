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
# link = input("Введите ссылку сайта: ")
link = 'https://www.redfin.com/city/1826/MA/Boston'

class Scraper:
    def __init__(self, url):
        main_html = self.get_html(url)
        self.soup = BeautifulSoup(main_html, 'html.parser')


    def get_html(self, url):
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
        papka_ind = 0
        try:
            os.mkdir(path + '/osnova')
        except FileExistsError:
            pass
        path2 = f'{path}/osnova'
        rest = []
        csv_file = []
        path_for_img = []
        time.sleep(2)
        picture_blocks = self.soup.find_all('div', class_='bottomV2')

        list_price = None
        pricesqqft = None
        est_mo_payment = None
        buyers_crokerage_compensation = None
        redfin_estimate = None
        hoa_dues = None
        status = None
        time_on_redfin = None
        property_type = None
        year_built = None
        style = None
        community = None
        lot_size = None
        mls = None

        for block in picture_blocks:
            loko = []
            try:
                os.mkdir(path2 + '/' + str(papka_ind))
            except FileExistsError:
                pass
            path3 = path2 + f'/{papka_ind}'
            path_for_img.append([path3])
            oson = block.a
            page_url = oson["href"]
            page_url = 'https://www.redfin.com' + page_url
            opa = self.get_html(page_url)
            page_soup_html = BeautifulSoup(opa, 'html.parser')
            # # Скачивание картин
            blocks_img = page_soup_html.find_all('img', class_ = 'landscape')
            for img_block in blocks_img:
                img_link = img_block["src"]
                # os.system(f'wget {img_link} -P {path3}')
            papka_ind += 1
        # # Price Insights & Home Facts
            osnova = page_soup_html.find_all('div', class_='keyDetail font-weight-roman font-size-base')
            for norm_or_none in osnova:
                norm_or_none1 = norm_or_none.text
                if 'List Price' in norm_or_none1:
                    list_price = norm_or_none1[11:].replace(',','')
                if 'Price/Sq.Ft.' in norm_or_none1:
                    pricesqqft = norm_or_none1[13:].replace(',','')
                if 'Est. Mo. Payment' in norm_or_none1:
                    est_mo_payment= norm_or_none1[17:].replace(',','')
                if "Buyer's Bronorm_or_none1erage Commission" in norm_or_none1:
                    buyers_crokerage_compensation = norm_or_none1[28:]
                if 'Redfin Estimate' in norm_or_none1:
                    redfin_estimate = norm_or_none1[16:].replace(',','')
                if 'HOA Dues' in norm_or_none1:
                    hoa_dues = norm_or_none1[9:]
                if 'Status' in norm_or_none1:
                    status = norm_or_none1[6:]
                if 'Time on Redfin' in norm_or_none1:
                    time_on_redfin = norm_or_none1[14:]
                if 'Property Type' in norm_or_none1:
                    property_type = norm_or_none1[13:]
                if 'Year Built' in norm_or_none1:
                    year_built = norm_or_none1[10:]
                if 'Style' in norm_or_none1:
                    style = norm_or_none1[5:]
                if 'Community' in norm_or_none1:
                    community = norm_or_none1[9:]
                if 'Lot Size' in norm_or_none1:
                    lot_size = norm_or_none1[8:]
                if 'MLS#' in norm_or_none1:
                    mls = norm_or_none1[4:]

            csv_file.append([list_price, pricesqqft, est_mo_payment, buyers_crokerage_compensation, redfin_estimate, hoa_dues, status, time_on_redfin, property_type, year_built, style, community, lot_size, mls])
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
            commis = page_soup_html.find_all('span', class_ = 'statsValue')
            for com in commis:
                ar = com.text
                loko.append(ar)
            rest.append(loko)
        with open(f'{path}/infa.csv', 'a') as csvfile:
            wr = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
            wr.writerow(['Addres','Price','Bedrooms','Bathrooms','Rest','List Price','Price Sq.Ft','Est. Mo. Payment','Buyer','Redfin estimate','HOA Dues','Status','Time on Redfin','Property Type','Year Built','Style','Community','Lot Size','MLS#','Path_for_img','Brokerage Compensation'])
            for i in range(len(csv_file)):
                wr.writerow(rest[i] + csv_file[i] + path_for_img[i])
            # yield csv_file

def amount_of_pages():
    time.sleep(2)
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
    except (requests.exceptions.ConnectionError, ValueError):
        print('Неправильно введен URL!')
    
# https://www.redfin.com/city/1826/MA/Boston
# windscribe connect
# windscribe login
# Windscribe Username: MinorRoosterLegislator

scraper = Scraper(link)
scraper.main_link()

# sa = []
# try:
#     for page in range(1, amount_of_pages()+1):
#         html = f'{link}/page-{page}'
#         scraper = Scraper(html)
#         scraper.main_link()
#         a = scraper.main_link()
#         for i in a:
#             sa.append(i)
# except (requests.ConnectionError):
#         print('Ошибка соединение с сервером!')
# except (TypeError):
#     pass

# if sa:
#     bd_password = input("Введите пароль от Базы Данных: ")

#     conn = psycopg2.connect(
#         dbname='postgres', 
#         user='postgres', 
#         password=bd_password, 
#         host='localhost'
#     )

#     cursor = conn.cursor()

#     cursor.execute('''CREATE TABLE redfin(
#         id SERIAL PRIMARY KEY, 
#         List Price VARCHAR(30) NOT NULL, 
#         Price Sq.Ft VARCHAR(30) NOT NULL, 
#         Est. Mo. Payment VARCHAR(30) NOT NULL, 
#         Buyer's Brokerage VARCHAR(30) NOT NULL, 
#         Redfin estimate VARCHAR(30) NOT NULL,
#         HOA Dues VARCHAR(30) NOT NULL,
#         Home Facts VARCHAR(30) NOT NULL,
#         Status VARCHAR(30) NOT NULL,
#         Time on Redfin VARCHAR(30) NOT NULL,
#         Property Type VARCHAR(30) NOT NULL,
#         Year Built VARCHAR(30) NOT NULL,
#         Style VARCHAR(30) NOT NULL,
#         Community VARCHAR(30) NOT NULL,
#         Lot Size VARCHAR(30) NOT NULL,
#         Style VARCHAR(30) NOT NULL,
#         MLS# VARCHAR(30) NOT NULL);'''
#     )


#     query = '''INSERT INTO freehtml5(List Price, Price Sq.Ft, Est. Mo. Payment, Buyer's Brokerage, Redfin estimate, HOA Dues, Home Facts, Status, Time on Redfin, Property Type, Year Built, Style, MLS#) VALUES '''

#     for index in range(len(sa)):
#         query += f'''(
#     \'{a[index][index]}\',
#     \'{a[index][index]}\',
#     \'{a[index][index]}\', 
#     \'{a[index][index]}\',
#     \'{a[index][index]}\',
#     \'{a[index][index]}\',
#     \'{a[index][index]}\',
#     \'{a[index][index]}\',
#     \'{a[index][index]}\',
#     \'{a[index][index]}\',
#     \'{a[index][index]}\',
#     \'{a[index][index]}\',
#     \'{a[index][index]}\',
            
#             ),'''

#     sql_query = query[:-1] + ';'


#     cursor.execute(sql_query)
#     conn.commit()



#     cursor.close()
#     conn.close()
# else:
#     pass
