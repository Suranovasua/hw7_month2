import sqlite3


# 1. Создать базу данных hw.db в sqlite через код python, используя модуль sqlite3
def connection(db_name):
    connect = None
    try:
        connect = sqlite3.connect(db_name)
    except sqlite3.Error as g:
        print(g)
    return connect


# 2. В БД создать таблицу products
def table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as g:
        print(g)


# 7. Добавить функцию, которая бы добавляла в БД 15 различных товаров
def insert_product(connetc, product):
    sql = '''
    INSERT INTO products (product_title,price,quantity)
    VALUES(?,?,?)
    '''
    try:
        cursor = connetc.cursor()
        cursor.execute(sql, product)
        connetc.commit()
    except sqlite3.Error as g:
        print(g)


# 8. Добавить функцию, которая меняет количество товара по id
def update_quantity(connect, product):
    sql = '''UPDATE products SET quantity=? WHERE id=?'''
    try:
        cursor = connect.cursor()
        cursor.execute(sql, product)
        connect.commit()
    except sqlite3.Error as g:
        print(g)


# 9. Добавить функцию, которая меняет цену товара по id
def update_price(connect, product):
    sql = '''UPDATE products SET price=? WHERE id=?'''
    try:
        cursor = connect.cursor()
        cursor.execute(sql, product)
        connect.commit()
    except sqlite3.Error as g:
        print(g)


# 11. Добавить функцию, которая бы выбирала все товары из БД и распечатывала бы их в консоли
def select_all_product(connect):
    sql = '''SELECT * FROM products'''
    try:
        cursor = connect.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()
        for i in row:
            print(i)
    except sqlite3.Error as g:
        print(g)


# 12. Добавить функцию, которая бы выбирала из БД товары,
# которые дешевле лимита (100 сом) сомов и
# количество которых больше чем лимит остатка на складе (5 шт) и
# распечатывала бы их в консоли
def select_limited_product(connect, price_limit, quantity_limit):
    sql = '''SELECT * FROM products WHERE price < ? and quantity > ?'''
    try:
        cursor = connect.cursor()
        cursor.execute(sql, (price_limit, quantity_limit))
        row = cursor.fetchall()
        for i in row:
            print(i)
    except sqlite3.Error as g:
        print(g)


# 10. Добавить функцию, которая удаляет товар по id
def delete(connect, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = connect.cursor()
        cursor.execute(sql, (id,))
        connect.commit()
    except sqlite3.Error as g:
        print(g)


# 13. Добавить функцию, которая бы искала в БД товары по названию (Например:
# искомое слово “мыло”, должны соответствовать поиску товары с названием -
# “Жидкое мыло с запахом ванили”, “Мыло детское” и тд.)
def search(connect, product):
    sql = '''SELECT * FROM products WHERE product_title LIKE ? '''
    try:
        cursor = connect.cursor()
        cursor.execute(sql, (product,))
        row = cursor.fetchall()
        for i in row:
            print(i)
    except sqlite3.Error as g:
        print(g)


# 2. В БД создать таблицу products
sql_create_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT (10,2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)'''

# 14. Протестировать каждую написанную функцию
my_connect = connection("hw.db")
if my_connect is not None:
    print("well done")
    # table(my_connect,sql_create_table)
    # insert_product(my_connect,("Apple",22,5))
    # insert_product(my_connect, ("Laptop", 800, 10))
    # insert_product(my_connect, ("Wireless Earbuds", 50, 20))
    # insert_product(my_connect, ("Smartphone", 600, 15))
    # insert_product(my_connect, ("Fitness Tracker", 80, 30))
    # insert_product(my_connect, ("Coffee Maker", 60, 12))
    # insert_product(my_connect, ("Backpack", 40, 25))
    # insert_product(my_connect, ("Digital Camera", 300, 8))
    # insert_product(my_connect, ("Portable Charger", 25, 50))
    # insert_product(my_connect, ("Bluetooth Speaker", 70, 18))
    # insert_product(my_connect, ("Gaming Mouse", 45, 15))
    # insert_product(my_connect, ("LED Desk Lamp", 30, 20))
    # insert_product(my_connect, ("Hiking Boots", 90, 10))
    # insert_product(my_connect, ("External Hard Drive", 100, 12))
    # insert_product(my_connect, ("Yoga Mat", 20, 35))
    # update_quantity(my_connect,(1,15))
    # update_price(my_connect,(1.99,1))
    # delete(my_connect,29)
    # select_all_product(my_connect)
    # select_limited_product(my_connect,100,5)
    # search(my_connect,'%camera%')
    my_connect.close()
