# -*- coding: utf-8 -*-
import tkinter as tk
import csv
import datetime
import os
import tkinter.font as tkFont
import pandas as pd
from __main__ import *

currentUser = userName.get()
today = str(datetime.date.today())
fileName = os.path.join(os.path.dirname(__file__), 'userinfo.csv')


def clearCSV():
    with open(fileName, 'w', encoding='utf-8') as csvfile:
        csvfile.truncate()
        csvfile.close()

def buttonexit_event():
    window.destroy()


def buttonagain_event():
    clearCSV()
    window.destroy()
    import main


def buttonrecord_event():
    import page4


def getfinallabel():  # 統計整天總攝取量
    totalmeal = [0] * 8
    with open(fileName, 'r', encoding='utf-8') as csvfile:
        lines = csvfile.readlines()
        for i in range(1, len(lines)):
            line = lines[i].split(',')
            if line[0] == today:
                if line[1] == (currentUser + '-'):
                    for j in range(8):
                        totalmeal[j] += float(line[j + 2])
        csvfile.close()
    for i in range(len(totalmeal)):
        totalmeal[i] = str(totalmeal[i])
    return totalmeal


def balancedornot():  # 統計各項是否均衡 #將兩類全榖雜糧和兩類油脂堅果合併統計
    balanced = []
    standard = [0.0] * 6
    typeseparated = [0.0] * 6
    bgColor = []
    with open(fileName, 'r', encoding='utf-8') as csvfile:
        lines = csvfile.readlines()
        for i in range(1, len(lines)):
            line = lines[i].split(',')
            if (line[0] == today) and (line[1] == currentUser):  # 找出標準(當天第一項)

                standard[0] = float(line[2]) + float(line[3])
                typeseparated[0] = float(totalmeal[0]) + float(totalmeal[1])
                for j in range(4, 8):
                    standard[j - 3] = float(line[j])
                    typeseparated[j - 3] = float(totalmeal[j - 2])
                standard[5] = float(line[8]) + float(line[9])
                typeseparated[5] = float(totalmeal[6]) + float(totalmeal[7])
        for k in range(6):
            if float(typeseparated[k]) > float(standard[k]):
                balanced.append("過量")
                bgColor.append('red')
            elif float(typeseparated[k]) < float(standard[k]):
                balanced.append("不足")
                bgColor.append('yellow')
            else:
                balanced.append("均衡")
                bgColor.append('limegreen')
        csvfile.close()
    for i in range(len(typeseparated)):
        typeseparated[i] = str(typeseparated[i])
    for i in range(len(standard)):
        standard[i] = str(standard[i])
    return bgColor, balanced, typeseparated, standard


slogan = [["主食吃太多會消化不良、體重直線上升！請注意飲食均衡喲！",
           "主食吃太少不行，運動做事會沒力氣的！再多吃一些補足精氣神！",
           "很棒！請繼續保持，你就是主食攝取小達人！"],
          ["蛋白質食物攝取太多可能會導致三高，也會造成腎臟的負擔！請注意飲食均衡喲！",
           "蛋白質食物攝取不夠，可能讓肌肉發育不佳或代謝速度變慢喲！快去吃些高蛋白質的食物補充元氣！",
           "真不錯！請繼續保持，你就是蛋白質攝取小達人！"],
          ["乳品攝取太多的話，是有可能讓膽固醇超標，進而增加心臟負擔的！請注意飲食均衡喲！",
           "乳品攝取不足會讓骨質變得脆弱、肌肉也可能流失！快去喝杯牛奶補齊營養素！",
           "你最棒！請繼續保持，你就是乳品攝取小達人！"],
          ["蔬菜吃得好多，很棒！但同時要記得飲食均衡的重要，各項營養素要多方攝取，才能擁有健康強壯的身體！",
           "蔬菜吃得不夠是個大問題！不僅會消化不良，更可能讓癌症因子找上門！每餐都要吃到一個拳頭份量的青菜喔！",
           "恭喜你！請繼續保持，你就是蔬菜攝取小達人！"],
          ["水果吃得好多，叫你水果大師！但攝取過多水果可能會導致糖份攝取過量，也要多多注意飲食均衡喲！",
           "水果吃得不夠會讓身體無法得到應有的維生素和營養，之後嘗試每餐都來點飯後水果吧！",
           "了不起！請繼續保持，你就是水果攝取小達人！"],
          ["油脂攝取過量了喔！攝取過多油脂可能增加某些癌症的發病風險，也可能成為揮之不去的肥肉！請注意飲食均衡喲！",
           "油脂類攝取不足，會影響體內維生素吸收，更會讓皮膚看來暗黃粗糙！可以每天來一把堅果，補足一天油脂的攝取！",
           "叫你第一名！請繼續保持，你就是油脂攝取小達人！"]]


def sloganchoose():
    sloganlist = []
    for i in range(len(balanced)):
        if balanced[i] == "過量":
            sloganlist.append(slogan[i][0])
        elif balanced[i] == "不足":
            sloganlist.append(slogan[i][1])
        else:
            sloganlist.append(slogan[i][2])
    return sloganlist


# 視窗設定
window = tk.Tk()

window_width = 900
window_height = 750
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')  # 視窗大小
window.title('均衡飲食計算機')  # 視窗標題
window.resizable(0, 0)  # 視窗大小可調整範圍 0=無範圍
window.configure(bg='pink')

# 物件設定
# labelFinish初始化
maintext = tk.StringVar()
totalmeal = getfinallabel()
bgColor, balanced, typeseparated, standard = balancedornot()
sloganlist = sloganchoose()
# 物件label
font1 = tkFont.Font(family='Arial', size=10)  # family:字型；slant:斜體；weight:粗體
font2 = tkFont.Font(family='Courier', size=12, slant='italic', weight='bold')
font3 = tkFont.Font(family='Courier', size=10, slant='italic', weight='bold')

tk.Label(window, text='你今天總共吃了~', bg='pink', font=font1).pack(pady=(0, 0))
tk.Label(window, text='全穀雜糧類(未精製) ' + totalmeal[0] + ' 碗', bg='pink', font=font1).pack()
tk.Label(window, text='全穀雜糧類(其他) ' + totalmeal[1] + ' 碗', bg='pink', font=font1).pack()
tk.Label(window, text='全穀雜糧類(總計) ' + typeseparated[0] + ' 碗/ '
                      + standard[0] + '碗', bg='pink', font=font1).pack()
tk.Label(window, text=balanced[0], bg=bgColor[0], font=font3).pack()
tk.Label(window, text=sloganlist[0] + "\n", bg='pink', font=font2).pack()

tk.Label(window, text='豆魚蛋肉類 ' + totalmeal[2] + ' 份/'
                      + standard[1] + ' 份  ', bg='pink', font=font1).pack()
tk.Label(window, text=balanced[1], bg=bgColor[1], font=font3).pack()
tk.Label(window, text=sloganlist[1] + "\n", bg='pink', font=font2).pack()

tk.Label(window, text='乳品 ' + totalmeal[3] + ' 杯/'
                      + standard[2] + ' 杯  ', bg='pink', font=font1).pack()
tk.Label(window, text=balanced[2], bg=bgColor[2], font=font3).pack()
tk.Label(window, text=sloganlist[2] + "\n", bg='pink', font=font2).pack()

tk.Label(window, text='蔬菜 ' + totalmeal[4] + '份/'
                      + standard[3] + ' 份  ', bg='pink', font=font1).pack()
tk.Label(window, text=balanced[3], bg=bgColor[3], font=font3).pack()
tk.Label(window, text=sloganlist[3] + "\n", bg='pink', font=font2).pack()

tk.Label(window, text='水果 ' + totalmeal[5] + ' 份/'
                      + standard[4] + ' 份  ', bg='pink', font=font1).pack()
tk.Label(window, text=balanced[4], bg=bgColor[4], font=font3).pack()
tk.Label(window, text=sloganlist[4] + "\n", bg='pink', font=font2).pack()

tk.Label(window, text='油脂類 ' + totalmeal[6] + ' 茶匙', bg='pink', font=font1).pack()
tk.Label(window, text='堅果種子 ' + totalmeal[7] + ' 份', bg='pink', font=font1).pack()
tk.Label(window, text='油脂與堅果種子類(總計) ' + typeseparated[5] + ' 份/'
                      + standard[5] + ' 份  ', bg='pink', font=font1).pack()
tk.Label(window, text=balanced[5], bg=bgColor[5], font=font3).pack()
tk.Label(window, text=sloganlist[5] + "\n", bg='pink', font=font2).pack()

# 按鈕
tk.Button(window, text='查看紀錄', width='8', height='1', command=buttonrecord_event, font=font1).pack(pady=(5, 5))
tk.Button(window, text='重新計算', width='8', height='1', command=buttonagain_event, font=font1).pack(pady=(0, 5))
tk.Button(window, text='離開', width='8', height='1', command=buttonexit_event, font=font1).pack(pady=(0, 5))
window.mainloop()
