import numpy as np
from scipy import integrate
import pandas as pd
import csv

#最小値   自動で取得するプログラムを組む
#MAX_min = 31097

#配列宣言
csv_input = []

#csvファイルを指定
MyPath = 'sample.csv'

#csvファイルを読み込み
with open(MyPath) as f:
    reader = csv.reader(f)
    #csvファイルのデータをループ
    for row in reader:
        #B列を配列へ格納
        csv_input.append(int(row[1]))

#csv_input = pd.read_csv("sample.csv",header=None, usecols=[1])
#print(csv_input)
#print(np.sum(csv_input))

dx_dt = csv_input
dt = 1
xt = 0.
x = []
count = 0
for dxt_dt in range(len(dx_dt)-1):
#for dxt_dt in range(100):

#    print(dxt_dt)
    if count == 10:
        x.append(xt)
        xt = 0
        count = 0
#    xt += dx_dt[dxt_dt] * dt

    xt += ((dx_dt[dxt_dt] + dx_dt[dxt_dt+1]) * dt) / 2
    xy = ((dx_dt[dxt_dt] + dx_dt[dxt_dt + 1]) * dt) / 2
    print(xy)
    count += 1
print(x)

#print(np.sum(x))