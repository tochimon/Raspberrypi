# -*- coding: utf-8 -*-
import smbus
import time
import datetime
import numpy as np

#グローバル変数
#窓用配列
list_raw = []
list_seki = []
num=1000 #窓の大きさ指定
for i in range(num):
    list_raw.insert(0,0)
    list_seki.insert(0,0)


now = datetime.datetime.now()
filename_raw = './rawdata/rawdata_' + now.strftime('%Y%m%d_%H%M') + '.csv'
filename_data = './data/data_' + now.strftime('%Y%m%d_%H%M') + '.csv'
print(now.strftime('%Y%m%d_%H') + '.csv')


def sekibun(data):
    sum = 0
    for i in range(len(data)-1):
        sum += (data[i] + data[i+1]) * 1 / 2
    return sum



def csvinput(filename,data):
    f = open(filename, 'a')
    f.write(str(data) + "\n")
    f.close()

def timer(before_time):
    now_time = time.time()
#   print(now_time)
    data = papils()
    csvinput(filename_raw,data)
    if (now_time - before_time >= 0.1):
        before_time = now_time
#       print(now_time)
        print(data)
        list_raw.insert(0, data)
        list_raw.pop(num)
        list_seki.insert(0,sekibun(list_raw))
        csvinput(filename_data,str(np.sum(list_seki)))
    return before_time

def papils():
        #コマンドフォーマット　アドレス　読み込みたいデータのアドレス　データ数
        #    rawdata=i2c.read_i2c_block_data(addr,addr,1)
        rawdata = i2c.read_word_data(addr, addr)
        #    rawdata = i2c.read_byte_data(addr, addr)
        return rawdata




#デバイスのアドレス 0x48
addr = 0x48
#count=1
i2c = smbus.SMBus(1)
time_sta = time.time()
before_time = time_sta

while 1:
    before_time = timer(before_time)