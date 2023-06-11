from database.data_base import get_name_price_foot, get_full_menu_name_price, post_basket_name, post_basket_count
from handlers.default_heandlers.basket import get_basket
from loader import bot
from telebot.types import Message, CallbackQuery
from keyboards.inline_button import menu_button, foot_button, drinks_button, count_product
from state.state_user import UserState
from utils.utils import list_callback

@bot.message_handler(commands=['menu'])
def menu_command(massage: Message):
    bot.send_message(chat_id=massage.from_user.id, text='Выберите категорию меню', reply_markup=menu_button())

@bot.callback_query_handler(func=lambda call: call.data == 'foot')
def foot_menu(call: CallbackQuery):
    """Вывод меню с продуктами"""
    bot.edit_message_text('Выберите продукт', chat_id=call.message.chat.id,
                          message_id=call.message.message_id, reply_markup=foot_button())

@bot.callback_query_handler(func=lambda call: call.data == 'drinks')
def foot_menu(call: CallbackQuery):
    """Вывод меню с напитками"""
    bot.send_message(call.message.chat.id, 'Выберите напиток', reply_markup=drinks_button())

@bot.callback_query_handler(func=lambda call: call.data in list_callback())
def add_basket(call: CallbackQuery):
    """Добавление в корзину товара и его сумму"""
    bot.set_state(user_id=call.from_user.id, state=UserState.count, chat_id=call.message.chat.id)
    with bot.retrieve_data(user_id=call.from_user.id, chat_id=call.message.chat.id) as data:
        data['product'] = str(call.data.split('_')[0])
    post_basket_name(name_price=call.data, user_id=call.from_user.id)
    bot.edit_message_text('Выберите количество из предложенных или напишите его',
                          chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          reply_markup=count_product())
@bot.message_handler(state=UserState.count)
def add_count_state(messages: Message):
    """Добавление количество товара из сообщения"""
    if messages.text.isdigit():
        with bot.retrieve_data(user_id=messages.from_user.id, chat_id=messages.chat.id) as data:
            post_basket_count(name=data['product'], count=int(messages.text), user_id=messages.from_user.id)
            bot.send_message(chat_id=messages.chat.id,
                             text=f'Вы добавили - <b>{data["product"]}</b> \n'
                                  f'количество - <b>{messages.text}</b>',
                             parse_mode='html',
                             reply_markup=menu_button())

@bot.callback_query_handler(func=lambda call: call.data.startswith('count'))
def add_count_callback(call: CallbackQuery):
    """Добавление количество товара по кнопке"""
    count = call.data.split('_')[1]
    with bot.retrieve_data(user_id=call.from_user.id, chat_id=call.message.chat.id) as data:
        name = data['product']
        post_basket_count(name=data['product'], count=int(count), user_id=call.from_user.id)
        bot.edit_message_text(text=f'Вы добавили - <b>{name}</b> \n'
                                   f'количество - <b>{count}</b>',
                              chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              parse_mode='html',
                              reply_markup=menu_button())

