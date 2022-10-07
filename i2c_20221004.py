# -*- coding: utf-8 -*-

import smbus
import time
from time import sleep
import datetime
import time

#デバイスのアドレス 0x48
addr = 0x48
#count=1
i2c = smbus.SMBus(1)
count=0
sleeptime = 0

time_sta = time.time()

while i2c:
#コマンドフォーマット　アドレス　読み込みたいデータのアドレス　データ数
#    rawdata=i2c.read_i2c_block_data(addr,addr,1)
    rawdata = i2c.read_word_data(addr, addr)
#    rawdata = i2c.read_byte_data(addr, addr)

    data = [str(count) + " " +str(rawdata) +"\n"]
    now = datetime.datetime.now()
    filename = './data/rawdata_' + now.strftime('%Y%m%d_%H%M') + '.csv'
    f= open(filename,'a')
    for line in data:
        f.write(line)
    f.close()
    print(rawdata)
    count+=1
    sleep(sleeptime)

    #10秒で終了
    if(time.time() - time_sta >= 10):
        break