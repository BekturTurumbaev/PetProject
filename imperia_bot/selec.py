import psycopg2

conn = psycopg2.connect(
    dbname='imperia', 
    user='postgres', 
    password='05052005', 
    host='localhost')
cursor = conn.cursor()

def sta():
    cmd = 'SELECT description FROM vacancies'
    cursor.execute(cmd)
    table_name = cursor.fetchall()
    for t in table_name:
        ans1 = str(table_name[0]).replace("'","").replace('(','').replace(')','')
        ans2 = str(table_name[1]).replace("'","").replace('(','').replace(')','')
        ans3 = str(table_name[2]).replace("'","").replace('(','').replace(')','')

    return ans1, ans2, ans3


def breakfast():
    names = 'SELECT names FROM breakfast'
    cursor.execute(names)
    table_name = cursor.fetchall()
    name = []
    for t in table_name:
        name.append(t[0])

    image_path = 'SELECT images_path FROM breakfast'
    cursor.execute(image_path)
    table_path = cursor.fetchall()
    img_path = []
    for a in table_path:
        img_path.append(a[0])

    prices = 'SELECT prices FROM breakfast'
    cursor.execute(prices)
    table_price = cursor.fetchall()
    price = []
    for m in table_price:
        price.append(m[0])

    return name, img_path, price

def pizza():
    names = 'SELECT names FROM pizza_40_cm'
    cursor.execute(names)
    table_name = cursor.fetchall()
    name = []
    for t in table_name:
        name.append(t[0])

    image_path = 'SELECT images_path FROM pizza_40_cm'
    cursor.execute(image_path)
    table_path = cursor.fetchall()
    img_path = []
    for a in table_path:
        img_path.append(a[0])

    prices = 'SELECT prices FROM pizza_40_cm'
    cursor.execute(prices)
    table_price = cursor.fetchall()
    price = []
    for m in table_price:
        price.append(m[0])

    return name, img_path, price

def roll():
    names = 'SELECT names FROM rolls'
    cursor.execute(names)
    table_name = cursor.fetchall()
    name = []
    for t in table_name:
        name.append(t[0])

    image_path = 'SELECT images_path FROM rolls'
    cursor.execute(image_path)
    table_path = cursor.fetchall()
    img_path = []
    for a in table_path:
        img_path.append(a[0])

    prices = 'SELECT prices FROM rolls'
    cursor.execute(prices)
    table_price = cursor.fetchall()
    price = []
    for m in table_price:
        price.append(m[0])

    return name, img_path, price

def salad():
    names = 'SELECT names FROM salads'
    cursor.execute(names)
    table_name = cursor.fetchall()
    name = []
    for t in table_name:
        name.append(t[0])

    image_path = 'SELECT images_path FROM salads'
    cursor.execute(image_path)
    table_path = cursor.fetchall()
    img_path = []
    for a in table_path:
        img_path.append(a[0])

    prices = 'SELECT prices FROM salads'
    cursor.execute(prices)
    table_price = cursor.fetchall()
    price = []
    for m in table_price:
        price.append(m[0])

    return name, img_path, price

def snack():
    names = 'SELECT names FROM snacks'
    cursor.execute(names)
    table_name = cursor.fetchall()
    name = []
    for t in table_name:
        name.append(t[0])

    image_path = 'SELECT images_path FROM snacks'
    cursor.execute(image_path)
    table_path = cursor.fetchall()
    img_path = []
    for a in table_path:
        img_path.append(a[0])

    prices = 'SELECT prices FROM snacks'
    cursor.execute(prices)
    table_price = cursor.fetchall()
    price = []
    for m in table_price:
        price.append(m[0])

    return name, img_path, price