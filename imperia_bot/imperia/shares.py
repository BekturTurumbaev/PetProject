import psycopg2
import os 
import json
from bs4 import BeautifulSoup
import shutil

class Shares:
    def shar(self):
        html_path = os.listdir(path='/home/asus/Desktop/mypizza.kg/Shares/ShareItem')
        all_shares = []
        try:
            shutil.rmtree('/home/asus/Desktop/imperia/shares_img')
        except FileNotFoundError:
            pass
        for html in html_path:
            header_op = []
            with open(f'/home/asus/Desktop/mypizza.kg/Shares/ShareItem/{html}', 'r') as t:
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
                    img = os.system(f'wget {path_img} -P /home/asus/Desktop/imperia/shares_img')
            osnova = []
            osnova = [i.replace('\n', '').replace('                                            ',' ') for i in header_op]
            all_shares.append(osnova)
        yield all_shares


shares = Shares()
shares_func = [share for share in shares.shar()]

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
    description TEXT NOT NULL,
    images VARCHAR(80) NOT NULL);'''
cursor.execute(cmd_1)

query = 'INSERT INTO share(headers, description, images) VALUES '
for i in range(len(shares_func[0])):
    query += f'(\'{shares_func[0][i][0]}\', \'{shares_func[0][i][1]}\', \'{shares_func[0][i][2]}\'),'

sql_query = query[:-1] + ';'

cursor.execute(sql_query)
conn.commit()   

cursor.close()
conn.close()

