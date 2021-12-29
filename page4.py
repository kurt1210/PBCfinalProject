# -*- coding: utf-8 -*-
import tkinter as tk
import csv
import datetime
import os
from __main__ import *

currentUser = userName.get()
fileName = os.path.join(os.path.dirname(__file__), 'userinfo.csv')


def buttonexit_event():
    window.destroy()


def findrecord():
    record = []
    today = str(datetime.date.today())
    yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'))
    recordstring = ''
    # 開啟csv找出今天和昨天的飲食紀錄(-),找到存入record待用
    with open(fileName, 'r', encoding='utf-8') as csvfile:
        lines = csvfile.readlines()
        for i in range(1, len(lines)):
            line = lines[i].split(',')
            if (line[0] == today) or (line[0] == yesterday):
                if line[1] == (currentUser + '-'):
                    record.append(line)
        csvfile.close()
    for j in range(len(record)):
        temp = str(record[j][0]) + ' 全穀雜糧' + str(float(record[j][2]) + float(record[j][3])) + '碗' + ' 豆蛋魚肉類' + str(
            float(record[j][4])) + '份' + ' 乳品' + str(float(record[j][5])) + '份' + ' 蔬菜' + str(
            float(record[j][6])) + '份' + ' 水果' + str(
            float(record[j][7])) + '份' + ' 油脂與堅果種子類' + str(float(record[j][8]) + float(record[j][9])) + '份\n'
        recordstring += temp
    return recordstring


# 視窗設定
window = tk.Tk()
window_width = 650
window_height = 350
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')  # 視窗大小（寬x長)
window.title('均衡飲食計算機')  # 視窗標題
window.resizable(0, 0)  # 視窗大小可調整範圍 0=無範圍
window.configure(bg='pink')

tk.Label(window, text=findrecord(), bg='pink').pack(pady=(20, 10))
tk.Button(window, text='關閉', width='8', height='1', command=buttonexit_event).pack(pady=(0, 5))

window.mainloop()
