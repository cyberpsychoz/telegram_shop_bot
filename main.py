import telebot

# создаем экземпляр бота, указывая токен
bot = telebot.TeleBot('ВАШ ТОКЕН СЮДА')

# создаем словарь товаров, где ключ - название товара, значение - цена товара
items = {
    'item1': 10,
    'item2': 20,
    'item3': 30
}

# обработчик команды /start, выводящий приветственное сообщение
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Добро пожаловать в наш магазин! Напишите /items, чтобы увидеть список товаров.')

# обработчик команды /items, выводящий список товаров
@bot.message_handler(commands=['items'])
def send_items(message):
    response = 'Список товаров:\n\n'
    for item, price in items.items():
        response += f'{item}: {price} руб.\n'
    bot.reply_to(message, response)

# обработчик сообщений с текстом, содержащим название товара, обрабатывающий покупку товара
@bot.message_handler(func=lambda message: message.text in items)
def buy_item(message):
    item = message.text
    price = items[item]
    # TODO: здесь нужно добавить логику оплаты товара
    bot.reply_to(message, f'Вы купили {item} за {price} руб.')

# запускаем бота
bot.polling()