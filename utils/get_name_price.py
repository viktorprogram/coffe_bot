from typing import List

from database import data_base

def list_callback():
    data = data_base.get_full_menu_name_price()
    list_callback_data = [f'{name}_{price}' for name, price in data]
    return list_callback_data
