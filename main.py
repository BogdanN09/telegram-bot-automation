import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

# Вставь сюда свой токен
bot = telegram.Bot(token='7783872604:AAHCxg7-_2ItRC1Tilx39_hCaxwDb4ncW0c')  # Замените на свой токен
chat_id = '@cryptowave_daily'  # Замените на свой канал

def send_message():
    bot.send_message(chat_id=chat_id, text="Ваше сообщение")

# Запуск планировщика для автоматической отправки сообщений
scheduler = BlockingScheduler()
scheduler.add_job(send_message, 'interval', minutes=10)  # Публиковать каждые 10 минут
scheduler.start()
