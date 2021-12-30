# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import os
import pandas as pd
import datetime
from __main__ import *

currentUser = userName.get()
fileName = os.path.join(os.path.dirname(__file__), 'userinfo.csv')
today = str(datetime.date.today())


def putdatatocsv():
    thismeal = [today, (currentUser + '-'), combo0.get(), combo1.get(), combo2.get(), combo3.get(), combo4.get(),
                combo5.get(), combo6.get(), combo7.get()]
    dataframe = pd.DataFrame(data=[thismeal])
    dataframe.to_csv(fileName, mode='a', header=False, index=False)


def combotozero():
    combo0.current(0)
    combo1.current(0)
    combo2.current(0)
    combo3.current(0)
    combo4.current(0)
    combo5.current(0)
    combo6.current(0)
    combo7.current(0)


def buttoninfo_event():
    import table2


def buttonsub_event():
    putdatatocsv()
    temp = getdefaultlabel()
    maintext.set(
        currentUser + '你好!今天還可以吃\n全穀雜糧類(未精製)' + temp[0] + '碗，全穀雜糧類(其他)' + temp[1] + '碗，豆魚蛋肉類' + temp[2] + '份，乳品' +
        temp[3] + '杯\n蔬菜' + temp[4] + '份，水果' + temp[5] + '份，油脂類' + temp[6] + '茶匙，堅果種子' + temp[
            7] + '份唷')
    combotozero()


def buttontotal_event():
    if (combo0.get() != '0') or (combo1.get() != '0') or (combo2.get() != '0') or (combo3.get() != '0') or (
            combo4.get() != '0') or (combo5.get() != '0') or (combo6.get() != '0') or (combo7.get() != '0'):
        putdatatocsv()
    window.destroy()
    import page3


def buttonexit_event():
    window.destroy()


def getdefaultlabel():
    tempplus = []
    tempminus = [0] * 8
    with open(fileName, 'r', encoding='utf-8') as csvfile:
        lines = csvfile.readlines()
        for i in range(1, len(lines)):
            line = lines[i].split(',')
            if line[0] == today:
                if line[1] != (currentUser + '-'):
                    for j in range(2, 10):
                        tempplus.append(float(line[j]))
                else:
                    for j in range(8):
                        tempminus[j] -= float(line[j + 2])
        csvfile.close()
    temp = list(map(lambda x: x[0] + x[1], zip(tempplus, tempminus)))
    for i in range(len(temp)):
        if temp[i] <= 0:
            temp[i] = '0'
        else:
            temp[i] = str(temp[i])

    return temp


# 視窗設定
window = tk.Tk()

window_width = 500
window_height = 550
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')  # 視窗大小（寬x長)
window.title('均衡飲食計算機')  # 視窗標題
window.resizable(0, 0)  # 視窗大小可調整範圍 0=無範圍
window.configure(bg='pink')

# 物件設定
# main label初始化
maintext = tk.StringVar()
labellist = getdefaultlabel()
maintext.set(
    currentUser + '你好!今天還可以吃~\n全穀雜糧類(未精製)' + labellist[0] + '碗，全穀雜糧類(其他)' + labellist[1] + '碗，豆魚蛋肉類' + labellist[
        2] + '份，乳品' + labellist[
        3] + '杯\n蔬菜' + labellist[4] + '份，水果' + labellist[5] + '份，油脂類' + labellist[6] + '茶匙，堅果種子' + labellist[7] + '份唷')

# 物件label&選單
font1 = tkFont.Font(family='Arial', size=9)

nums = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
tk.Button(window, text='info', command=buttoninfo_event, font=font1).pack(side=tk.LEFT, anchor=tk.NW, padx=(0, 0))
tk.Label(window, textvariable=maintext, bg='pink', font=font1).pack(pady=(20, 10))
tk.Label(window, text='全穀雜糧類(未精製/碗)', bg='pink', font=font1).pack()
combo0 = ttk.Combobox(window, values=nums, state='readonly')  # 全穀雜糧類(未精製/碗)選單
combo0.pack()
tk.Label(window, text='全穀雜糧類(其他/碗)', bg='pink', font=font1).pack()
combo1 = ttk.Combobox(window, values=nums, state='readonly')  # 全穀雜糧類(其他/碗)選單
combo1.pack()
tk.Label(window, text='豆魚蛋肉類(份)', bg='pink', font=font1).pack()
combo2 = ttk.Combobox(window, values=nums, state='readonly')  # 豆魚蛋肉類(份)選單
combo2.pack()
tk.Label(window, text='乳品(杯)', bg='pink', font=font1).pack()
combo3 = ttk.Combobox(window, values=nums, state='readonly')  # 乳品(杯)選單
combo3.pack()
tk.Label(window, text='蔬菜(份)', bg='pink', font=font1).pack()
combo4 = ttk.Combobox(window, values=nums, state='readonly')  # 蔬菜(份)選單
combo4.pack()
tk.Label(window, text='水果(份)', bg='pink', font=font1).pack()
combo5 = ttk.Combobox(window, values=nums, state='readonly')  # 水果(份)選單
combo5.pack()
tk.Label(window, text='油脂類(茶匙)', bg='pink', font=font1).pack()
combo6 = ttk.Combobox(window, values=nums, state='readonly')  # 油脂類(茶匙)選單
combo6.pack()
tk.Label(window, text='堅果種子(份)', bg='pink', font=font1).pack()
combo7 = ttk.Combobox(window, values=nums, state='readonly')  # 堅果種子(份)選單
combo7.pack()
combotozero()

# 按鈕
tk.Button(window, text='subtotal', width='6', height='1', command=buttonsub_event, font=font1).pack(pady=(10, 5))
tk.Button(window, text='total', width='6', height='1', command=buttontotal_event, font=font1).pack(pady=(0, 5))
tk.Button(window, text='exit', width='6', height='1', command=buttonexit_event, font=font1).pack(pady=(0, 5))

window.mainloop()
