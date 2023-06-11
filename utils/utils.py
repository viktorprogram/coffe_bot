from typing import List

from database import data_base
from database.data_base import get_basket_db


def list_callback():
    """Получения списка колбеков"""
    data = data_base.get_full_menu_name_price()
    list_callback_data = [f'{name}_{price}' for name, price in data]
    return list_callback_data

def basket_utils(user_id) -> str:
    """Корзина с товарами пользователя"""
    basket = get_basket_db(user_id)
    str_basket = ''
    full_price = 0
    for name, price, count, price_count in basket:
        str_basket += f'<b>{name}</b> - {count} шт. = {price_count} ₽ \n'
        full_price += price_count
    return f'Ваша корзина\n {str_basket}\n итого : <b>{full_price} ₽ </b>'
