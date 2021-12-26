# -*- coding: utf-8 -*-
import tkinter as tk
import csv
import datetime

today = str(datetime.date.today())

def buttonexit_event():
    window.destroy()

def buttonagain_event():
    with open('userinfo.csv', 'w', encoding='utf-8') as csvfile:
        csvfile.truncate()
        csvfile.close()
    window.destroy()
    import main


def getfinallabel():  # 統計整天總攝取量
    totalmeal = [0] * 8
    with open('userinfo.csv', 'r', encoding='utf-8') as csvfile:
        lines = csvfile.readlines()
        for i in range(1, len(lines)):
            line = lines[i].split(',')
            if line[0] == today:
                if line[1] == '-':
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
    with open('userinfo.csv', 'r', encoding='utf-8') as csvfile:
        lines = csvfile.readlines()
        for i in range(1, len(lines)):
            line = lines[i].split(',')
            if line[0] == today:  # 找出標準(當天第一項)
                standard[0] = float(line[2]) + float(line[3])
                typeseparated[0] = float(totalmeal[0]) + float(totalmeal[1])
                for j in range(4, 8):
                    standard[j - 3] = float(line[j])
                    typeseparated[j - 3] = float(totalmeal[j - 2])
                standard[5] = float(line[8]) + float(line[9])
                typeseparated[5] = float(totalmeal[6]) + float(totalmeal[7])
            for j in range(6):
                if float(typeseparated[j]) > float(standard[j]):
                    balanced.append("過量")
                elif float(typeseparated[j]) < float(standard[j]):
                    balanced.append("不足")
                else:
                    balanced.append("均衡")
            break
        csvfile.close()
    for i in range(len(typeseparated)):
        typeseparated[i] = str(typeseparated[i])
    for i in range(len(standard)):
        standard[i] = str(standard[i])
    return balanced, typeseparated, standard


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
window.geometry('650x600')  # 視窗大小（寬x長)
window.title('均衡飲食計算機')  # 視窗標題
window.resizable(0, 0)  # 視窗大小可調整範圍 0=無範圍

# 物件設定
# labelFinish初始化
maintext = tk.StringVar()
totalmeal = getfinallabel()
balanced, typeseparated, standard = balancedornot()
sloganlist = sloganchoose()
# 物件label

tk.Label(window, text='今天總共吃了\n').grid(column=0, row=0)

tk.Label(window, text='全穀雜糧類(未精製)').grid(column=0, row=2)
tk.Label(window, text=totalmeal[0] + '碗').grid(column=1, row=2)
tk.Label(window, text='全穀雜糧類(其他)').grid(column=0, row=3)
tk.Label(window, text=totalmeal[1] + '碗').grid(column=1, row=3)
tk.Label(window, text='全穀雜糧類(總計)').grid(column=0, row=4)
tk.Label(window, text=typeseparated[0] + '碗/' + standard[0] + '碗').grid(column=1, row=4)
tk.Label(window, text=balanced[0]).grid(column=2, row=4)
tk.Label(window, text=sloganlist[0] + "\n").grid(column=0, columnspan=20, row=5, sticky=tk.W)

tk.Label(window, text='豆魚蛋肉類').grid(column=0, row=6)
tk.Label(window, text=totalmeal[2] + '份/' + standard[1] + '份').grid(column=1, row=6)
tk.Label(window, text=balanced[1]).grid(column=2, row=6)
tk.Label(window, text=sloganlist[1] + "\n").grid(column=0, columnspan=20, row=7, sticky=tk.W)

tk.Label(window, text='乳品').grid(column=0, row=8)
tk.Label(window, text=totalmeal[3] + '杯/' + standard[2] + '杯').grid(column=1, row=8)
tk.Label(window, text=balanced[2]).grid(column=2, row=8)
tk.Label(window, text=sloganlist[2] + "\n").grid(column=0, columnspan=20, row=9, sticky=tk.W)

tk.Label(window, text='蔬菜').grid(column=0, row=10)
tk.Label(window, text=totalmeal[4] + '份/' + standard[3] + '份').grid(column=1, row=10)
tk.Label(window, text=balanced[3]).grid(column=2, row=10)
tk.Label(window, text=sloganlist[3] + "\n").grid(column=0, columnspan=20, row=11, sticky=tk.W)

tk.Label(window, text='水果').grid(column=0, row=12)
tk.Label(window, text=totalmeal[5] + '份/' + standard[4] + '份').grid(column=1, row=12)
tk.Label(window, text=balanced[4]).grid(column=2, row=12)
tk.Label(window, text=sloganlist[4] + "\n").grid(column=0, columnspan=20, row=13, sticky=tk.W)

tk.Label(window, text='油脂類').grid(column=0, row=14)
tk.Label(window, text=totalmeal[6] + '茶匙').grid(column=1, row=14)
tk.Label(window, text='堅果種子').grid(column=0, row=15)
tk.Label(window, text=totalmeal[7] + '份').grid(column=1, row=15)
tk.Label(window, text='油脂與堅果種子類(總計)').grid(column=0, row=16)
tk.Label(window, text=typeseparated[5] + '份/' + standard[5] + '份').grid(column=1, row=16)
tk.Label(window, text=balanced[5]).grid(column=2, row=16)
tk.Label(window, text=sloganlist[5] + "\n").grid(column=0, columnspan=20, row=17, sticky=tk.W)

# 按鈕
tk.Button(window, text='查看紀錄').grid(column=0, row=20)
tk.Button(window, text='重新計算', command=buttonagain_event).grid(column=0, row=21)
tk.Button(window, text='離開', command=buttonexit_event).grid(column=0, row=22)
window.mainloop()
