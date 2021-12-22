# -*- coding: utf-8 -*-
import tkinter as tk
import csv

def buttonagain():
    with open('userinfo.csv', 'w', encoding='utf-8') as csvfile:
        csvfile.truncate()
        csvfile.close()
    window.destroy()
    import main

def getfinallabel():
    return '還沒寫'


# 視窗設定
window = tk.Tk()
window.geometry('500x550')  # 視窗大小（寬x長)
window.title('均衡飲食計算機')  # 視窗標題
window.resizable(0, 0)  # 視窗大小可調整範圍 0=無範圍

# 物件設定
# labelFinish初始化
maintext = tk.StringVar()
labellist = getfinallabel()
maintext.set(labellist)
# 物件label
tk.Label(window, textvariable=maintext).grid(column=0, row=0)

# 按鈕
tk.Button(window, text='重新計算', command=buttonagain).grid(column=0, row=1)

window.mainloop()
