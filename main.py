import os
import telebot
import random

# Список возможных "Схем по заработку"
schemes = [
    "Как заработать миллион за неделю",
    "Как стать популярным блогером",
    "Как создать свой криптовалютный стартап",
    "Как инвестировать в недвижимость",
    "Как стать успешным фрилансером"
]

# Стоимость одной "Схемы по заработку" в рублях
price = 1000

# Создаем объект бота с помощью токена, полученного от @BotFather
bot = telebot.TeleBot("ВАШ ТОКЕН")

# Обработчик команд /start и /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # Отправка приветственного сообщения и инструкций
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Я бот магазина по продаже 'Схем по заработку'. Чтобы узнать список доступных схем, введите /list. Чтобы купить схему, введите /buy номер_схемы. Например, /buy 1.")

# Обработчик команды /list
@bot.message_handler(commands=['list'])
def send_list(message):
    # Отправка списка доступных схем с номерами и ценами
    text = "Список доступных схем:\n\n"
    for i, scheme in enumerate(schemes):
        text += f"{i+1}. {scheme} - {price} руб.\n"
    bot.send_message(message.chat.id, text)

# Обработчик команды /buy
@bot.message_handler(commands=['buy'])
def send_buy(message):
    # Проверка корректности номера схемы
    try:
        # Получение номера схемы из сообщения
        number = int(message.text.split()[1])
        # Проверка диапазона номера
        if 1 <= number <= len(schemes):
            # Получение названия схемы по номеру
            scheme = schemes[number-1]
            # Отправка сообщения с подтверждением покупки и ссылкой на оплату
            bot.send_message(message.chat.id, f"Вы выбрали схему '{scheme}'. Чтобы оплатить ее, перейдите по ссылке: https://pay.com/{BOT_TOKEN}/{number}")
        else:
            # Отправка сообщения об ошибке
            bot.send_message(message.chat.id, f"Неверный номер схемы. Введите число от 1 до {len(schemes)}.")
    except (IndexError, ValueError):
        # Отправка сообщения об ошибке
        bot.send_message(message.chat.id, "Неверный формат команды. Введите /buy номер_схемы.")

# Обработчик всех остальных сообщений
@bot.message_handler(func=lambda msg: True)
def send_default(message):
    # Отправка сообщения с подсказкой
    bot.send_message(message.chat.id, "Я не понимаю ваше сообщение. Введите /help, чтобы узнать список команд.")

# Запуск бота
bot.polling()
