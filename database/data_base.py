import sqlite3


def get_name_price_foot(name: str):
    """Запрос на название и цену еды или напитков"""
    if name == 'foot':
        category = 2
    elif name == 'drinks':
        category = 1
    db_menu = sqlite3.connect(r'database\\db_menu')
    curs = db_menu.cursor()
    curs.execute(f'SELECT name, price FROM menu WHERE category = {category}')
    data = curs.fetchall()
    curs.close()
    return data

def get_full_menu_name_price():
    """Запрос на все названия """
    db_menu = sqlite3.connect(r'database\\db_menu')
    curs = db_menu.cursor()
    curs.execute(f'SELECT name, price FROM menu')
    data = curs.fetchall()
    curs.close()
    return data

def post_basket_name(name_price: str, user_id):
    """Добавление товара в корзину"""
    name_, price = name_price.split('_')
    db_menu = sqlite3.connect(r'database\\db_menu')
    curs = db_menu.cursor()
    if not curs.execute(f"SELECT id FROM Basket WHERE name_id = (SELECT id FROM menu WHERE name = '{name_}') AND user_id  = '{user_id}'").fetchall():
        curs.execute(f"INSERT INTO Basket (name_id, price, user_id) "
                     f"VALUES ("
                     f"(SELECT id FROM menu WHERE name = '{name_}'), "
                     f"'{price}', "
                     f"'{user_id}')"
                     )
    else:
        curs.close()
        return
    db_menu.commit()
    curs.close()

def post_basket_count(name: str, count: int, user_id):
    """Добавление количества продуктов"""
    db_menu = sqlite3.connect(r'database\\db_menu')
    curs = db_menu.cursor()
    curs.execute(f"UPDATE Basket SET count = count + {count} "
                 f"WHERE name_id = (SELECT id FROM menu WHERE name = '{name}') "
                 f"and user_id = '{user_id}'")
    db_menu.commit()
    curs.close()

def get_basket_db(user_id):
    """Вывод корзины с общей ценой"""
    db_menu = sqlite3.connect(r'database\\db_menu')
    curs = db_menu.cursor()
    curs.execute(f"SELECT name, Basket.price, count, (Basket.price * Basket.count) FROM Basket "
                 f"JOIN menu ON menu.id = Basket.name_id "
                 f"WHERE Basket.user_id = '{user_id}'")
    data = curs.fetchall()
    curs.close()
    return data

def cleaning_basket_db(user_id):
    db_menu = sqlite3.connect(r'database\\db_menu')
    curs = db_menu.cursor()
    curs.execute(f"SELECT COUNT(*) FROM Basket WHERE user_id = {user_id}")
    count = curs.fetchall()
    curs.execute(f"DELETE FROM Basket WHERE user_id = {user_id}")
    db_menu.commit()
    curs.close()
    return count