import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

# Настройки для бота

# Торговая пара и таймфрейм
SYMBOL = "BTC_USDT"
INTERVAL = "Min1"  # 1 минута для контрактов

# REST API endpoint для свечей
MEXC_KLINES_URL = "https://contract.mexc.com/api/v1/contract/kline"

# Telegram настройки
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
MEXC_API_KEY = os.getenv("MEXC_API_KEY")
MEXC_API_SECRET = os.getenv("MEXC_API_SECRET")