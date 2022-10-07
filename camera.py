# coding: utf-8
import RPi.GPIO as GPIO
import time
import datetime
import os
import subprocess
def camera():
    ## ポートの初期化（人感センサの準備）
    PORT_SWITCH = 24
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PORT_SWITCH, GPIO.OUT, initial=GPIO.LOW)

    ## 保存ディレクトリの設定
    SAVEDIR = './Pictures'
    if not os.path.isdir(SAVEDIR):
        os.makedirs(SAVEDIR)

    ## メインループ

    hour = datetime.datetime.now().hour
    # print(hour)
    if hour <= 6 or hour >= 17:
        GPIO.output(PORT_SWITCH, 1)
        time.sleep(1)
    # GPIO.output(PORT_SWITCH, 1)

    # 撮影（raspistill + raspividコマンドの外部呼び出し）
    now = 'log_' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = os.path.join(SAVEDIR, now)
    cmd = 'raspistill -o ' + filename + '.jpg' + ' -t 2000 -w 1024 -h 768'
    subprocess.call(cmd, shell=True)

    cmd = 'cp ' + filename + '.jpg' + ' ' + os.path.join(SAVEDIR, 'image.jpg')
    subprocess.call(cmd, shell=True)

    print('Filename: ' + filename + 'Date: ' + now)

    time.sleep(1)
    GPIO.output(PORT_SWITCH, 0)

    # time.sleep(10)
    GPIO.cleanup()

    return 0
