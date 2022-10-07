# -*- coding: utf-8 -*-
import smbus
import time
import datetime
import numpy as np
import csv

#グローバル変数
#窓用配列
list_raw = []
list_seki = []

#窓の大きさ指定
num = 50
#データ取得の幅
dt = 0.1

#積分用
for i in range(num):
    list_raw.insert(0, 0)
    list_seki.insert(0, 0)
sum_seki = 0


now = datetime.datetime.now()
filename_raw = './rawdata/rawdata_' + now.strftime('%Y%m%d_%H%M') + '.csv'
filename_data = './data/data_' + now.strftime('%Y%m%d_%H%M') + '.csv'
print(now.strftime('%Y%m%d_%H') + '.csv')

#datafileの項目名
f = open(filename_data, mode='a', newline="")
f.write("raw,integrl,average,integrl-average\n")
f.close()

#デバイスのアドレス 0x48
addr = 0x48
i2c = smbus.SMBus(1)
time_sta = time.time()
before_time = time_sta

def sekibun(data, sum_seki):
    list_seki.insert(0, ((data[0] + data[1]) * dt) / 2)
    sum_seki += list_seki[0]  # 積分値追加
    sum_seki -= list_seki[num - 1]  # 古い積分値削除
    list_seki.pop(num)
    return sum

def ave(data):
    sum = 0
    for i in range(len(data)):
        sum += data[i]
    ave = sum / num
    return ave

def csvinput(filename,data):
    f = open(filename, mode='a', newline="")
    f.write(str(data))
    f.write("\n")
    f.close()

def papils():
    #コマンドフォーマット　アドレス　読み込みたいデータのアドレス　データ数
    #    rawdata=i2c.read_i2c_block_data(addr,addr,1)
    #rawdata = i2c.read_word_data(addr, addr)
    rawdata = i2c.read_byte_data(addr, addr)
    return rawdata

while 1:
    now_time = time.time()
#   print(now_time)
    data = papils()
    csvinput(filename_raw, data)
    if now_time - before_time >= dt:
        before_time = now_time
#       print(now_time)
#        print(data)
        list_raw.insert(0, data)
        list_raw.pop(num)
#        seki_data = sekibun(list_raw,sum_seki)
#        print(sum_seki)

        list_seki.insert(0, ((list_raw[0] + list_raw[1]) * dt) / 2)
        sum_seki += list_seki[0]  # 積分値追加
        sum_seki -= list_seki[num - 1]  # 古い積分値削除
        list_seki.pop(num)

#        ave_data = ave(list_raw)

        ave_data = (np.sum(list_raw)) / num

        csvdata = (str(data) + "," + str(sum_seki)+"," + str(ave_data) + "," + str(sum_seki-ave_data))
        print(csvdata)
        csvinput(filename_data, csvdata)