# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import csv
import os
from firstinput import info
import datetime
import pandas as pd

# def buttoninfo_event():
#     import table1

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

window_width = 400
window_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')  # 視窗大小
window.title('均衡飲食計算機')  # 視窗標題
window.resizable(0, 0)  # 視窗大小可調整範圍 0=無範圍
window.configure(bg='pink')

# 物件設定
# 物件本人
entryName = tk.Entry(window,bg='white') #  姓名欄
comboGender = ttk.Combobox(window, values=['男', '女'], state='readonly')  # 性別選單
comboGender.current(0)  # 性別選單預設項目
comboAge = ttk.Combobox(window, values=['19-30', '31-50', '51-70', '71+'], state='readonly')  # 年齡選單
comboAge.current(0)  # 年齡選單預設項目
comboActivity = ttk.Combobox(window, values=['低', '稍低', '適度', '高'], state='readonly')  # 活動強度選單
comboActivity.current(0)  # 活動強度選單預設項目

# 物件label&物件
tk.Label(window, text='姓名', bg='pink').pack(pady=(75, 0)) #  姓名label
entryName.pack() #  姓名欄位置
tk.Label(window, text='性別', bg='pink').pack() #  性別label
comboGender.pack() #  性別選單位置
tk.Label(window, text='年齡', bg='pink').pack() #  年齡label
comboAge.pack() #  年齡選單位置
tk.Label(window, text='活動強度', bg='pink').pack() #  活動強度label
comboActivity.pack() #  活動強度選單位置

# 按鈕
tk.Button(window, text='OK', command=buttonOK_event).pack(pady=(10,5))
# tk.Button(window, text='info', command=buttoninfo_event).pack(side=tk.LEFT, anchor=tk.SE, padx=(0,0))
window.mainloop()