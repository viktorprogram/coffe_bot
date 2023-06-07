import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

DEFAULT_COMMANDS = (
    ('start', 'Запуск бота'),
    ('menu', 'Вывести меню'),
    ('basket', 'Вывести корзину'),
    ('help', 'Вывести справку'),
    ('hy', 'кака я то команда'),
)