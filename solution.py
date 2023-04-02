import pandas as pd
import numpy as np


chat_id = 419670097  # Ваш chat ID, не меняйте название переменной


def solution(x: np.array) -> float:
    ans_arr = np.exp(x)
    return ans_arr.mean()  # Ваш ответ
