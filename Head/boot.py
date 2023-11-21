#テスト用boot
#研究室wifiには接続せず，受け取った内容を表示するだけ

import os
import network
import machine
from machine import Pin, SoftI2C
import utime
import webrepl
import urequests
from password import *

SSID_NAME_LAB = ['CDSL-A910-11n']

p2 = Pin(2, Pin.OUT)

def wifiscan(): #スキャンしたwifiのリストを返す．
    global wifi
    wifiList = wifi.scan()
    wifiAPDict = []
    for wl in wifiList:
        if wl[0].decode('utf-8') != '':
            wifiAPDict.append(wl[0].decode('utf-8'))
    return wifiAPDict

def connect_lab_wifi(timeout = 10):
    global wifi
    if wifi.ifconfig()[0].split(".")[0] == "192":
        wifi.disconnect()
    else:
        pass
    
    endFlag = False
    wifiName = wifiscan()
    print(wifiName)

    for wn in wifiName:
        if wn in SSID_NAME_LAB:
            print(f"[{wn}]に接続します")
            wifi.connect(wn, lab_wifi_pass)
            while True:
                
                if wifi.ifconfig()[0].split(".")[0] == "192":
                    p2.on()
                    endFlag = True
                    print("----  wifi is connected -----")
                    print(f"----[{wifi.ifconfig()[0]}]に接続----")
                    webrepl.start(password = webrepl_pass)
                    break
                else:
                    utime.sleep(1)
            if endFlag == True:
                break
        if endFlag == True:
            break

machine.freq(240000000)

ap = None

wifiStatus = True
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

print('boot is ok')
for i in range(3):
    p2.on()
    p2.off()

#execfile("current.py")
execfile("main.py")
utime.sleep(1)