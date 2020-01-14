import csv
import pandas as pd
import numpy as np
from collections import Counter

# 로또 당첨 숫자 분석
# 숫자별 당첨 횟수, 확률
# 숫자 조합

if __name__ == '__main__':
    dataset = pd.read_csv('lotto.csv', thousands=',', header=None, encoding='utf-8')
    # print(dataset.iloc[3, 26:])
    # print(dataset.shape)
    # print(dataset.iloc[:, -7:])
    lotto = dataset.iloc[3:, -7:]
    print(lotto)
    lotto_list = []
    for i in range(dataset.index):
        for j in range(dataset.columns):
            num = dataset.loc[i, j]
            lotto_list.append(num)

    # lotto_list = [dataset.loc[i, j] for i in dataset.index for j in dataset.columns]
    print(lotto_list)
    # count = Counter(lotto)
    # print(count)

