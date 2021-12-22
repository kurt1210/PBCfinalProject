# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import csv
import os
from firstinput import info
import datetime
import pandas as pd

def buttonOK_event():
    fileName = 'userinfo.csv'

    if not os.path.exists(fileName):
        with open(fileName, 'w', encoding='utf-8') as csvfile:
            csvfile.close()

    #行頭
    field = ['Time', 'Name', 'F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7']
    today = str(datetime.date.today())
    #產生使用者合適的標準
    uf = info(today, entryName.get(), comboGender.current(), comboAge.current(), comboActivity.current())
    #如果檔案為空寫入使用者資料
    if os.path.getsize(fileName) == 0:
        dataframe = pd.DataFrame(data=[uf], columns=field)
        dataframe.to_csv(fileName, index=False)
        window.destroy()
        import page2
    #檔案內有資料
    else:
        dataframe = pd.read_csv(fileName)
        for i in range(len(dataframe)):
            currentusername = entryName.get()
            #使用者是否存在,存在則判斷今天有無使用,有則直接進下一頁,無則放入新一天的標準
            if dataframe['Name'][i] == currentusername:
                if dataframe['Time'][i] == today:
                    window.destroy()
                    import page2
                else:
                    dataframe = pd.DataFrame(data=[uf])
                    dataframe.to_csv(fileName, mode='a', header=False, index=False)
                    window.destroy()
                    import page2
                #使用者不存在寫入使用者資料
            else:
                dataframe = pd.DataFrame(data=[uf])
                dataframe.to_csv(fileName, mode='a', header=False, index=False)
                window.destroy()
                import page2




#視窗設定
window = tk.Tk()
window.geometry('400x400')  # 視窗大小
window.title('均衡飲食計算機')  # 視窗標題
window.resizable(0, 0)  # 視窗大小可調整範圍 0=無範圍

# 物件設定
# 物件label
tk.Label(window, text='姓名').grid(column=0, row=0) #  姓名label
tk.Label(window, text='性別').grid(column=0, row=3) #  性別label
tk.Label(window, text='年齡').grid(column=0, row=6) #  年齡label
tk.Label(window, text='活動強度').grid(column=0, row=9) #  活動強度label
# 物件本人
entryName = tk.Entry(window,bg='dark grey') #  姓名欄
comboGender = ttk.Combobox(window, values=['男', '女'], state='readonly')  # 性別選單
comboGender.current(0)  # 性別選單預設項目
comboAge = ttk.Combobox(window, values=['19-30', '31-50', '51-70', '71+'], state='readonly')  # 年齡選單
comboAge.current(0)  # 年齡選單預設項目
comboActivity = ttk.Combobox(window, values=['低', '稍低', '適度', '高'], state='readonly')  # 活動強度選單
comboActivity.current(0)  # 活動強度選單預設項目
# 按鈕
tk.Button(window, text='OK', command=buttonOK_event).grid(column=0, row=12)
# 物件位置
entryName.grid(column=0, row=1) #  姓名欄位置
comboGender.grid(column=0, row=4) #  性別選單位置
comboAge.grid(column=0, row=7) #  年齡選單位置
comboActivity.grid(column=0, row=10) #  活動強度選單位置

window.mainloop()