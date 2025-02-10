import telebot
import sqlite3

bot = telebot.TeleBot('7736265547:AAGnxKHv45qdeeWHlMqrWE_VzGPLCnfl0fw')

@bot.message_handler(commands=['start'])
def start(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn1 = types.KeyboardBatton('Зарегистрироваться')
  btn2 = types.KeyboardBatton('Авторизоваться')
  markup.add(btn1, btn2)
  bot.send_message(message.chat.id, 'Здравствуйте! Выберете действие'
