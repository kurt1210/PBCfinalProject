# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import pandas as pd
import datetime

fileName = 'userinfo.csv'
today = str(datetime.date.today())


def buttonsub_event():
    thismeal = [today, '-', combo0.get(), combo1.get(), combo2.get(), combo3.get(), combo4.get(), combo5.get(),
                combo6.get(), combo7.get()]
    dataframe = pd.DataFrame(data=[thismeal])
    dataframe.to_csv(fileName, mode='a', header=False, index=False)
    temp = getdefaultlabel()
    maintext.set(
        '今天還可以吃\n全穀雜糧類(未精製)' + temp[0] + '碗，全穀雜糧類(其他)' + temp[1] + '碗，豆魚蛋肉類' + temp[2] + '份，乳品' +
        temp[3] + '杯\n蔬菜' + temp[4] + '份，水果' + temp[5] + '份，油脂類' + temp[6] + '茶匙，堅果種子' + temp[
            7] + '份')


def buttontotal_event():
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
                if line[1] != '-':
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
window.geometry('500x550')  # 視窗大小（寬x長)
window.title('均衡飲食計算機')  # 視窗標題
window.resizable(0, 0)  # 視窗大小可調整範圍 0=無範圍

# 物件設定
# main label初始化
maintext = tk.StringVar()
labellist = getdefaultlabel()
maintext.set(
    '今天還可以吃\n全穀雜糧類(未精製)' + labellist[0] + '碗，全穀雜糧類(其他)' + labellist[1] + '碗，豆魚蛋肉類' + labellist[2] + '份，乳品' + labellist[
        3] + '杯\n蔬菜' + labellist[4] + '份，水果' + labellist[5] + '份，油脂類' + labellist[6] + '茶匙，堅果種子' + labellist[7] + '份')

# 物件label
tk.Label(window, textvariable=maintext).grid(column=0, row=0)
tk.Label(window, text='全穀雜糧類(未精製/碗)').grid(column=0, row=2)
tk.Label(window, text='全穀雜糧類(其他/碗)').grid(column=0, row=4)
tk.Label(window, text='豆魚蛋肉類(份)').grid(column=0, row=6)
tk.Label(window, text='乳品(杯)').grid(column=0, row=8)
tk.Label(window, text='蔬菜(份)').grid(column=0, row=10)
tk.Label(window, text='水果(份)').grid(column=0, row=12)
tk.Label(window, text='油脂類(茶匙)').grid(column=0, row=14)
tk.Label(window, text='堅果種子(份)').grid(column=0, row=16)

# 選單
nums = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
combo0 = ttk.Combobox(window, values=nums, state='readonly')  # 全穀雜糧類(未精製/碗)選單
combo0.current(0)  # 全穀雜糧類(未精製/碗)預設項目
combo1 = ttk.Combobox(window, values=nums, state='readonly')  # 全穀雜糧類(其他/碗)選單
combo1.current(0)  # 全穀雜糧類(其他/碗)預設項目
combo2 = ttk.Combobox(window, values=nums, state='readonly')  # 豆魚蛋肉類(份)選單
combo2.current(0)  # 豆魚蛋肉類(份)預設項目
combo3 = ttk.Combobox(window, values=nums, state='readonly')  # 乳品(杯)選單
combo3.current(0)  # 乳品(杯)預設項目
combo4 = ttk.Combobox(window, values=nums, state='readonly')  # 蔬菜(份)選單
combo4.current(0)  # 蔬菜(份)預設項目
combo5 = ttk.Combobox(window, values=nums, state='readonly')  # 水果(份)選單
combo5.current(0)  # 水果(份)預設項目
combo6 = ttk.Combobox(window, values=nums, state='readonly')  # 油脂類(茶匙)選單
combo6.current(0)  # 油脂類(茶匙)預設項目
combo7 = ttk.Combobox(window, values=nums, state='readonly')  # 堅果種子(份)選單
combo7.current(0)  # 堅果種子(份)預設項目

# 按鈕
tk.Button(window, text='subtotal', command=buttonsub_event).grid(column=0, row=18)
tk.Button(window, text='total', command=buttontotal_event).grid(column=0, row=19)
tk.Button(window, text='exit', command=buttonexit_event).grid(column=0, row=20)

# 物件位置
combo0.grid(column=0, row=3)
combo1.grid(column=0, row=5)
combo2.grid(column=0, row=7)
combo3.grid(column=0, row=9)
combo4.grid(column=0, row=11)
combo5.grid(column=0, row=13)
combo6.grid(column=0, row=15)
combo7.grid(column=0, row=17)
window.mainloop()
