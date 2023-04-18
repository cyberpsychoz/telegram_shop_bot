# Telegram Bot Shop

Это бот магазина по продаже "Схем по заработку" в Telegram. Бот предлагает пользователю выбрать одну из пяти схем и перейти по ссылке на оплату. После оплаты пользователь получает ссылку на скачивание схемы.

## Установка и запуск

Для установки и запуска бота вам понадобятся:

- Python 3.6 или выше
- Библиотека pyTelegramBotAPI
- Токен доступа к боту, полученный от BotFather

Склонируйте репозиторий или скачайте архив с исходным кодом:

```bash
git clone https://github.com/your_username/telegram-bot-shop.git
Перейдите в папку с проектом и установите зависимости:

cd telegram-bot-shop
pip install -r requirements.txt
Создайте файл .env и добавьте в него токен доступа к боту:

echo "BOT_TOKEN=your-bot-token-here" > .env
Запустите бота:

python bot.py
