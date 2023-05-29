from loader import bot
from telebot.types import Message

@bot.message_handler(commands=['menu'])
def menu_command(massage: Message):
    bot.send_message(chat_id=massage.from_user.id, text='Выберите категорию меню')