from loader import bot
from telebot.types import Message

@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    bot.reply_to(message, "<b>Добрый день</b>\n"
                          "Выберите одну из команд\n"
                          "/menu - меню\n"
                          "/basket - корзина с товаром", parse_mode='html')
