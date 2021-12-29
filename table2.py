import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

df = pd.DataFrame()
df['全穀雜糧類 1 碗 ( 碗為一般家用飯碗、重量為可食重量 )'] = ['= 糙米飯 1 碗 或 雜糧飯 1 碗 或 米飯 1 碗\n= 熟麵條 2 碗 或 小米稀飯 2 碗 或 燕麥粥 2 碗\n= 米、大麥、小麥、蕎麥、燕麥、麥粉、麥片 80 公克\n= 中型芋頭 4/5 個 (220 公克) 或 小蕃薯 2 個 (220 公克)\n= 玉米 2 又 2/3 根 (340 公克) 或 馬鈴薯 2 個 (360 公克)\n= 全麥饅頭 1 又 1/3 個 (120 公克)\n    或 全麥土司 2 片 (120 公克)' ]
df['豆魚蛋肉類 1 份 ( 重量為可食部分生重 )'] = ['= 黃豆 (20 公克) 或 毛豆 (50 公克) 或 黑豆 (25 公克)\n= 無糖豆漿 1 杯\n= 雞蛋 1 個\n= 傳統豆腐 3 格 (80 公克) 或 嫩豆腐半盒 (140 公克)\n   或 小方豆干 1 又 1/4 片 (40 公克)\n= 魚 (35 公克) 或 蝦仁 (50 公克)\n= 牡蠣 (65 公克) 或 文蛤 (160 公克) 或 白海蔘 (100 公克)\n= 去皮雞胸肉 (30 公克)\n    或 鴨肉、豬小里肌肉、羊肉、牛腱 (35 公克)']
df['乳品類 1 杯 ( 1 杯 = 240 毫升全脂、脫脂或低脂奶 = 1 份 )'] = ['= 鮮奶、保久乳、優酪乳 1 杯(240 毫升)\n= 全脂奶粉 4 湯匙(30 公克)\n= 低脂奶粉 3 湯匙(25 公克)\n= 脫脂奶粉 2.5 湯匙(20 公克)\n= 乳酪（起司）2 片(45 公克)\n= 優格 210 公克']

fig = plt.figure(figsize=(14, 6))
ax=plt.subplot(111)
ax.axis('off')

the_table1 = plt.table(cellText=[['全穀雜糧類 1 碗 ( 碗為一般家用飯碗、重量為可食重量 )', '豆魚蛋肉類 1 份 ( 重量為可食部分生重 )','乳品類 1 杯 ( 1 杯 = 240 毫升全脂、脫脂或低脂奶 = 1 份 )']],
                     loc='center',
                     cellLoc='center',
                     bbox=[0, 0.75, 1, 0.1]
                     )

the_table2 = plt.table(cellText=df.values,
                     loc='center',
                     cellLoc='left',
                     bbox=[0, 0.45, 1, 0.3]
                     )
the_table1.auto_set_font_size(False)
the_table1.set_fontsize(9)

the_table2.auto_set_font_size(False)
the_table2.set_fontsize(8)

plt.title('六大類食物代換份量')

df = pd.DataFrame()
df['蔬菜類 1 份 ( 1 份為可食部分生重約 100 公克 )'] = ['= 生菜沙拉 ( 不含醬料 )100 公克\n= 煮熟後相當於直徑 15 公分盤 1 碟，或 約大半碗\n= 收縮率較高的蔬菜如莧菜、地瓜葉等，煮熟後約占半碗\n= 收縮率較低的蔬菜如芥蘭菜、青花菜等，煮熟後約占 2/3 碗']
df['水果類 1 份( 1 份為切塊水果約大半碗 ~1 碗 )'] = ['= 可食重量估計約等於 100 公克 (80~120 公克)\n= 香蕉 ( 大 ) 半根 70 公克\n= 榴槤 45 公克']
df['油脂與堅果種子類 1 份 ( 重量為可食重量 )'] = ['= 芥花油、沙拉油等各種烹調用油 1 茶匙 (5 公克)\n= 杏仁果、核桃仁 (7 公克) 或 開心果、南瓜子、葵花子、\n   黑 (白) 芝麻、腰果 (10 公克) 或 各式花生仁 (13 公克)\n   或 瓜子 (15 公克 )\n= 沙拉醬 2 茶匙 (10 公克) 或 蛋黃醬 1 茶匙 (8 公克)']

the_table3 = plt.table(cellText=[['蔬菜類 1 份 ( 1 份為可食部分生重約 100 公克 )', '水果類 1 份 ( 1 份為切塊水果約大半碗 ~1 碗 ) ', '油脂與堅果種子類 1 份 ( 重量為可食重量 )']],
                     loc='center',
                     cellLoc='center',
                     bbox=[0, 0.3, 1, 0.1]
                     )
the_table4 = plt.table(cellText=df.values,
                     loc='center',
                     cellLoc='left',
                     bbox=[0, 0, 1, 0.3]
                     )
the_table3.auto_set_font_size(False)
the_table3.set_fontsize(9)

the_table4.auto_set_font_size(False)
the_table4.set_fontsize(8)

plt.show()