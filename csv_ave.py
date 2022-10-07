import numpy as np
from scipy import integrate
import pandas as pd
import csv

#配列宣言
csv_input = []

#csvファイルを指定
MyPath = 'soto.csv'

#csvファイルを読み込み
with open(MyPath) as f:
    reader = csv.reader(f)
    #csvファイルのデータをループ
    for row in reader:
        #B列を配列へ格納
        csv_input.append(int(row[0]))

print(csv_input)

s = 1000 #範囲　要実験
j = 0 #配列数
sum = 0 #範囲合計値
ave = [] #範囲平均値
count = 0 #繰り返し回数

for i in range(len(csv_input)-s-1):
    sum = 0
    for num in range(i,i+s):
        sum += csv_input[num]
    ave.append(sum/s)

    f_out = open('testfile_ave.csv', 'a')
    f_out.write(str(sum/s) + "\n")
    #        print(str(np.sum(list_seki)))
    f_out.close()

print(ave)