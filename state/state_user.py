from telebot.handler_backends import State, StatesGroup

class UserState(StatesGroup):
    basket = State()
    count = State()
    none = State()
