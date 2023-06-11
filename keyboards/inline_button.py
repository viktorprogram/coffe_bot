from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import sqlite3

from database.data_base import get_name_price_foot


# from database.data_base import db_menu

def menu_button() -> InlineKeyboardMarkup:
    """Набор кнопок для вывода категорий меню"""
    markup = InlineKeyboardMarkup()
    but_1 = InlineKeyboardButton('Еда', callback_data='foot')
    but_2 = InlineKeyboardButton('Напитки', callback_data='drinks')
    but_3 = InlineKeyboardButton('Корзина', callback_data='basket')
    markup.add(but_1, but_2, but_3)
    return markup

def foot_button() -> InlineKeyboardMarkup:
    """Набор кнопок для меню с едой"""
    but = [[InlineKeyboardButton(text=f'{name} {price} ₽', callback_data=f'{name}_{price}')]
           for name, price in get_name_price_foot('foot')]
    markup = InlineKeyboardMarkup(but, row_width=1)
    return markup

def drinks_button() -> InlineKeyboardMarkup:
    """Набор кнопок для меню с напитками"""
    but = [[InlineKeyboardButton(text=f'{name} {price} ₽', callback_data=f'{name}_{price}')]
           for name, price in get_name_price_foot('drinks')]
    markup = InlineKeyboardMarkup(but, row_width=1)
    return markup

def count_product() -> InlineKeyboardMarkup:
    """Кнопки количество товара"""
    markup = InlineKeyboardMarkup(row_width=2)
    but_1 = InlineKeyboardButton('1', callback_data='count_1')
    but_2 = InlineKeyboardButton('2', callback_data='count_2')
    but_3 = InlineKeyboardButton('3', callback_data='count_3')
    but_4 = InlineKeyboardButton('4', callback_data='count_4')
    markup.add(but_1, but_2, but_3, but_4)
    return markup

def cleaning_basket_button() -> InlineKeyboardMarkup:
    """Кнопка очистки корзины"""
    markup = InlineKeyboardMarkup()
    but_1 = InlineKeyboardButton('Очистить корзину', callback_data='cleaning')
    markup.add(but_1)
    return markup
