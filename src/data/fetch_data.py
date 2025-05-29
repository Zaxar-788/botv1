import requests
from config import SYMBOL, INTERVAL, MEXC_KLINES_URL


def get_latest_klines(limit=100):
    """
    Получить последние свечи (klines) по выбранной паре и таймфрейму
    с MEXC (контрактный API).
    Возвращает список свечей (OHLCV).
    """
    url = f"{MEXC_KLINES_URL}/{SYMBOL}"
    params = {
        "interval": INTERVAL,
        "limit": limit
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print(f"Ошибка получения данных: {response.status_code}")
        return []