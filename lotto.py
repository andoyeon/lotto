import csv
import pandas as pd
import numpy as np
from collections import Counter

# 로또 당첨 숫자 분석
# 숫자별 당첨 횟수, 확률
# 숫자 조합

if __name__ == '__main__':
    col_names = ['1', '2', '3', '4', '5', '6', 'bonus']
    dataset = pd.read_csv('lotto.csv', thousands=',', header=None, encoding='utf-8')
    print(dataset.shape)
    dataset = dataset.iloc[3:, -7:]
    print(dataset)
    dataset_except_bonus = dataset.iloc[:, :-1]
    print(dataset_except_bonus)

    # 단순 분석
    # 보너스 포함
    lotto_list = [dataset.loc[i, j] for i in dataset.index for j in dataset.columns]
    lotto_list = map(int, lotto_list)
    count = Counter(lotto_list)
    print(count)

    # 보너스 제외
    lotto_except_bonus_list = [dataset.loc[i, j] for i in dataset.index for j in dataset.columns]
    lotto_except_bonus_list = map(int, lotto_except_bonus_list)
    count = Counter(lotto_except_bonus_list)
    print(count)

