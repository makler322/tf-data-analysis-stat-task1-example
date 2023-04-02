import pandas as pd
import numpy as np


chat_id = 419670097  # Ваш chat ID, не меняйте название переменной


def solution(x: np.array) -> float:
    ans_arr = np.log(x - 299)
    return ans_arr.mean()  # Ваш ответ
