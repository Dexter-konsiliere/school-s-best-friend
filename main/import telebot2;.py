import telebot
import sqlite3


# создание таблицы
connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARU KEY, name TEXT NOT NULL, birth date TEXT NOT NULL, role TEXT NOT NULL)')
connection.commit()
connection.close()


bot = telebot.TeleBot('7736265547:AAGnxKHv45qdeeWHlMqrWE_VzGPLCnfl0fw')


name = ''
birth_date = ''


@bot.message_handler(commands=['start'])
def start(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn1 = types.KeyboardBatton('Зарегистрироваться')
  btn2 = types.KeyboardBatton('Авторизоваться')
  markup.add(btn1, btn2)
  bot.send_message(message.chat.id, 'Здравствуйте! Выберете действие'


# регистрация проходить при помощи одной команды и четырёх функций
@bot.message_handler(commands=['reg'])
def reg(message):
  bot.send_message(message.chat.id, 'Введите своё полное имя')
  bot.register_next_step_handler(message, user_name)


# запоминаем имя пользователя
def user_name(message):
  global name
  name = message.text.strip()
  bot.send_message(message.chat.id, 'Введите свою дату рождения в цыфрах')
  bot.register_next_step_handler(message, user_birth_date)


# запоминаем дату роджения
def user_birth_date(message):
  global birth_date
  birth_date = message.text.strip()
  bot.send_message(message.chat.id, 'Вы ученик или учитель?')
  bot.register_next_step_handler(message, user_role)


# запоминаем роль и добавляем все данные пользователя в таблицу
def user_role(message):
  role = message.text.strip()
  bot.send_message(message.chat.id, 'Отлично, вы зарегистрированы!')
  
  connection = sqlite3.connect('database.db')
  cursor = connection.cursor()
  cursor.execute('INSERT INTO Users (name, birth date, role) VALUES (?, ?, ?)', (name, birth_date, role))
  connection.commit()
  connection.close()

