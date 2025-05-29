import numpy as np


def is_volume_spike(klines, window=20, multiplier=2):
    """
    Проверяет, есть ли всплеск объёма на последней свече.
    Возвращает True, если объём последней свечи в 'multiplier' раз больше
    среднего за 'window' свечей.
    """
    if len(klines) < window + 1:
        return False
    # Объём — это 5-й элемент в каждом массиве свечи
    volumes = [float(k[5]) for k in klines[-(window+1):-1]]
    avg_volume = np.mean(volumes)
    last_volume = float(klines[-1][5])
    return last_volume > avg_volume * multiplier