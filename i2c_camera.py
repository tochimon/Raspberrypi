# -*- coding: utf-8 -*-

import smbus
import csv
import  time
import numpy as np
import camera

#import sleep

#デバイスのアドレス 0x48
addr = 0x48
#count=1
i2c = smbus.SMBus(1)
f= open('csvfile.csv','w')
f.close()
count=0

#100
list = []
for i in range(100):
    list.insert(0,0)
camera_flag=0

while i2c:
#コマンドフォーマット　アドレス　読み込みたいデータのアドレス　データ数
#    rawdata=i2c.read_i2c_block_data(addr,addr,1)
    rawdata = i2c.read_word_data(addr, addr)
#    rawdata = i2c.read_byte_data(addr, addr)

    list.insert(0,rawdata)
    del list[100]
#    print(list)

    deff = (int)(list[0]-list[99])
    if deff > 10000 and count>100 and camera_flag==0:
        print("camera")
        print(deff)
        camera_flag=1
        camera_flag = camera.camera()
        print(camera_flag)
    data = [str(count) + " " +str(rawdata) +"\n"]
    f= open('csvfile.csv','a')
    for line in data:
        f.write(line)
    f.close()
    print(rawdata )
    count+=1
#    sleep(0.5)
