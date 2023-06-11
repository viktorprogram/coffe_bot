from keyboards.inline_button import cleaning_basket_button
from loader import bot
from telebot.types import Message, CallbackQuery
from database.data_base import cleaning_basket_db
from utils.utils import basket_utils


@bot.message_handler(commands=['basket'])
def get_basket(messages: Message):
    """Вывод корзины по команде"""
    bot.send_message(chat_id=messages.chat.id,
                     text=basket_utils(user_id=messages.from_user.id),
                     reply_markup=cleaning_basket_button(),
                     parse_mode='html')

@bot.callback_query_handler(func=lambda call: call.data == 'basket')
def callback_basket(call: CallbackQuery):
    """Вывод корзины по нажатию кнопки"""
    bot.send_message(chat_id=call.message.chat.id,
                     text=basket_utils(user_id=call.from_user.id),
                     reply_markup=cleaning_basket_button(),
                     parse_mode='html')

@bot.callback_query_handler(func=lambda call: call.data == 'cleaning')
def cleaning_basket(call: CallbackQuery):
    """Очистка корзины"""
    count_delete = cleaning_basket_db(user_id=call.from_user.id)
    bot.send_message(chat_id=call.message.chat.id, text='Корзина очищена\n'
                                                        f'Удалено товара -  {count_delete[0][0]}')
