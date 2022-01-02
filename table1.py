# 安靜 = 0，站立 = 1，步行 = 2，快走 = 3，肌肉運動 = 4
# 低 <= 13，稍低 = 19，適度 = 23，高 >= 25

import io
from PIL import Image, ImageTk
import tkinter as tk
import os

def table1():

    def resize(w, h, w_box, h_box, pil_image):
        f1 = 1.0 * w_box / w
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        width = int(w * factor)
        height = int(h * factor)
        return pil_image.resize((width, height), Image.ANTIALIAS)


    window = tk.Toplevel()
    # 框的大小
    w_box = 500
    h_box = 650

    # 以PIL圖像打開
    pil_image = Image.open(os.path.join(os.path.dirname(__file__), 'image1.png'))

    # 圖片的原始大小
    w, h = pil_image.size

    # 縮放圖片使圖片在框內且保持比例
    pil_image_resized = resize(w, h, w_box, h_box, pil_image)

    # 把PIL圖像轉為Tkinter的PhotoImage
    tk_image = ImageTk.PhotoImage(pil_image_resized)

    label = tk.Label(window, image=tk_image, width=w_box, height=h_box)
    label.pack(padx=5, pady=5)  # 圖與邊緣的距離
    window.mainloop()