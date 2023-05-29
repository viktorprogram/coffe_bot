from telebot import TeleBot
from config_data import config
from telebot.storage import StateMemoryStorage

storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)

# @bot.message_handler(func=lambda message: True)
# def bot_start(message: Message):
#     bot.reply_to(message, message.text)
