import numpy as np
import csv
import datetime

#最小値   自動で取得するプログラムを組む
MAX_min = 18506

#配列宣言
csv_input = []

#csvファイルを指定
MyPath = 'soto.csv'
count = 0

#csvファイルを読み込み
with open(MyPath) as f_in:
    reader = csv.reader(f_in)
    #csvファイルのデータをループ
    for row in reader:
        #配列へ格納
        csv_input.append(int(row[0]))
f_in.close()

#csv_input = pd.read_csv("sample.csv",header=None, usecols=[1])
#print(csv_input)
#print(np.sum(csv_input))

dx_dt = csv_input

#積分後用変数
list_seki = []
dt = 1
xt = 0.
sum = 0



#窓用配列
list_raw = []
num=1000 #窓の大きさ指定
for i in range(num):
    list_raw.insert(0,0)
    list_seki.insert(0,0)

now = datetime.datetime.now()
#filename = str(now.strftime("%Y%m%d%H%M%S" + ".csv"))

filename = "./data/outputdata_2.csv"
print(filename)

for dxt_dt in range(len(dx_dt)-1):
#for dxt_dt in range(105): #test用

    rawdata = dx_dt[dxt_dt] #データを一つずつ出力
    list_raw.insert(0, rawdata-MAX_min)
    list_raw.pop(num)

    #逐次台形積分
    list_seki.insert(0,((list_raw[0] + list_raw[1]) * dt) / 2)
    list_seki.pop(num)
#    if dxt_dt >= num:
    if 1>0: #テスト用
        count += 1
        f_out = open(filename, 'a')
#        f_out = open("test_seki.csv", 'a')

        f_out.write(str(np.sum(list_seki)) + "\n")


#        print(str(np.sum(list_seki)))
        f_out.close()
#        print(np.sum(list_seki))

print(range(len(dx_dt)-1))
print(count)