import time
from data.fetch_data import get_latest_klines
from utils.helpers import is_volume_spike
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, SYMBOL, INTERVAL
import requests


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }
    response = requests.post(url, data=payload)
    print(f"Отправка в Telegram: {text}")
    print(f"Статус ответа Telegram: {response.status_code}, ответ: {response.text}")


def main():
    print("Бот запущен. Ожидание сигналов...")
    send_telegram_message("✅ Бот успешно запущен и готов к работе!")
    last_signal_time = 0
    print(f"TELEGRAM_TOKEN: {TELEGRAM_TOKEN}")
    print(f"TELEGRAM_CHAT_ID: {TELEGRAM_CHAT_ID}")
    while True:
        klines = get_latest_klines()
        if klines and is_volume_spike(klines):
            last_candle = klines[-1]
            price = last_candle[4]
            volume = last_candle[5]
            msg = (
                f"🚨 ВСПЛЕСК ОБЪЁМА!\n"
                f"Пара: {SYMBOL}_PERP\n"
                f"Таймфрейм: {INTERVAL}\n"
                f"Цена: {price}\n"
                f"Объём: {volume}\n"
                f"Рекомендация: наблюдать за рынком!"
            )
            # Чтобы не спамить, отправляем сигнал не чаще раза в 5 минут
            if time.time() - last_signal_time > 300:
                send_telegram_message(msg)
                last_signal_time = time.time()
        time.sleep(30)


if __name__ == "__main__":
    main()