from sys import version
import requests
import psycopg2
import os 
import csv
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        main_html = self.get_html(url)
        self.soup = BeautifulSoup(main_html, 'html.parser')

    def get_html(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            return r.text   
        elif r.status_code == 403:
            print('Вы заблокированы на этом сайте!')
            return 0
        elif r.status_code == 404:
            print('Страница не найдена!')
            return 0

    def main(self):
        path = os.path.dirname(os.path.abspath(__file__))
        try:
            os.mkdir(path + '/zip_files')
        except FileExistsError:
            pass

        img_link = []
        img_blocks = self.soup.find_all('img', class_ = 'card-img-top wp-post-image')
        for img_block in img_blocks:
            img_url = img_block["src"]
            img_link.append(img_url)

        headers = []
        header_blocks = self.soup.find_all('h2', class_ = 'entry-title')
        for header_block in header_blocks:
            header = header_block.a.text
            headers.append(header)

        dates = []
        date_blocks = self.soup.find_all('p', class_ = 'card-text post-meta')
        for date_block in date_blocks:
            date = date_block.small.text
            dates.append(' '.join(date.split(' ')[1:4]))

        download_and_views_blocks = self.soup.find_all('p', class_='card-text hits')

        downloads = []
        for download_block in download_and_views_blocks:   
            download1 = download_block.text.strip().replace(',','').split(' ')
            if len(download1) == 2:
                download1 = (f'0 Downloads {download1[0]}')
            download2 = download1[0]
            downloads.append(download2)

        views = []
        for views_block in download_and_views_blocks:
            view = views_block.text.replace(',', '').strip().split(' ')
            views.append(view[view.index('Views')-1])

        links = []
        depiction = []
        description_blocks = self.soup.find_all('a', class_ = 'img-link')
        for block in description_blocks:
            link = block["href"]
            links.append(link)

            link_for_page = self.get_html(link)
            soup_page = BeautifulSoup(link_for_page, 'html.parser')
            pairs = soup_page.find_all('div', class_='entry-content')
            for pas in pairs:
                descriptions = pas.p.text
                features_or_leave = pas.h2.text

                if features_or_leave == 'Leave your vote':
                    description = ''.join(descriptions) + ' 0'
                    depiction.append(description)
                else:# features_or_leave == 'Features':
                    features = pas.ul.text
                    description = ''.join(descriptions) + features
                    depiction.append(description)

            zip_pairs = soup_page.find_all('div', class_='single-demo-download')
            for zip_pair in zip_pairs:
                zip_link = zip_pair.a["href"]

            if 'p-preview' in zip_link:
                pass
            elif 'preview' in zip_link:
                html_zip = self.get_html(zip_link)
                soup_html = BeautifulSoup(html_zip, 'html.parser')
                zip_blocks = soup_html.find_all('a', class_='template-download countable_link')
                for zip_block in zip_blocks:
                    zip_downloads = zip_block["href"]
                os.system(f'wget {zip_downloads} -P {path}/zip_files')
        return img_link, headers, dates, downloads, views, links, depiction


def amount_of_pages():
    try:
        r = requests.get('https://freehtml5.co/') # Don't touch!!!
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            pagination = soup.find_all('a', class_='page-link')
            pages = []
            for block in pagination:
                span_block = block.text
                if span_block == '»':
                    pass
                else:
                    pages.append(int(span_block))
            return max(pages)

    except requests.ConnectionError:
        print('Ошибка соединение с сервером!')
try:
    bd_password = input("Введите пароль от Базы Данных: ")

    conn = psycopg2.connect(
        dbname='postgres', 
        user='postgres', 
        password=bd_password, 
        host='localhost')
    cursor = conn.cursor()

    cmd = "SELECT table_name FROM information_schema.tables WHERE table_name = 'freehtml5';"
    cursor.execute(cmd)
    table_name = cursor.fetchone()
    if 'freehtml5' == table_name[0]:
        cmd_0 = 'DROP TABLE freehtml5;'
        cursor.execute(cmd_0)
        conn.commit()
    cursor.execute('''CREATE TABLE freehtml5(
        id SERIAL PRIMARY KEY, 
        images VARCHAR(120) NOT NULL, 
        headers VARCHAR(120) NOT NULL, 
        dates VARCHAR(30) NOT NULL, 
        downloads VARCHAR(30) NOT NULL, 
        views VARCHAR(30) NOT NULL,
        links VARCHAR(120) NOT NULL,
        texts TEXT NOT NULL);''')
    conn.commit()

    for page in range(1, amount_of_pages()+1):
        scraper = Scraper(f'https://freehtml5.co/page/{page}/')
        all_ = [scrap for scrap in scraper.main()]

        query = 'INSERT INTO freehtml5(images, headers, dates, downloads, views, links, texts) VALUES '

        for index in range(len(all_)):
            query += f'(\'{all_[0][index]}\',\'{all_[1][index]}\',\'{all_[2][index]}\',\'{all_[3][index]}\',\'{all_[4][index]}\',\'{all_[5][index]}\',\'{all_[6][index]}\'),'
        sql_query = query[:-1] + ';'
        cursor.execute(sql_query)
        conn.commit()

        print(f'Страниц пропарсено: {page}')
    print('Все страницы успешно пропарсены!')
    cursor.close()
    conn.close()
except (requests.exceptions.ConnectionError):
        print('Неправильно введен URL!')
except (TypeError):
        pass