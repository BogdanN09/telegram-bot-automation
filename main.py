import os
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

# Получаем токен из переменной окружения
token = os.getenv('TELEGRAM_TOKEN')

bot = telegram.Bot(token=token)
chat_id = '@cryptowave_daily'  # Замените на свой канал

def send_message():
    bot.send_message(chat_id=chat_id, text="Ваше сообщение")

# Запуск планировщика для автоматической отправки сообщений
scheduler = BlockingScheduler()
scheduler.add_job(send_message, 'interval', minutes=10)  # Публиковать каждые 10 минут
scheduler.start()


