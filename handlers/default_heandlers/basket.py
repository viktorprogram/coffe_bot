from loader import bot
from telebot.types import Message, CallbackQuery
from database.data_base import get_basket

@bot.message_handler(commands=['basket'])
def basket(messages: Message):
    get_basket(user_id=messages.from_user.id)