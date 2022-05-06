import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
import wx


def histgram_main(file_path):
    img = cv2.imread(file_path)

    histgram_do(img)

    while True:
        cv2.imshow("Frame", img)

        key = cv2.waitKey(30)
        # enterキーで
        # 閉じるようにしてみる
        if key == 13:
            break

def histgram_do(img):
    color = ('b', 'g' , 'r')
    for i,col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color = col)
        plt.xlim([0, 256])

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    histr = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
    plt.plot(histr, color='orange')
    plt.show()


if __name__ == "__main__":
    app = wx.App()
    dialog = wx.FileDialog(None, u'動画像を選択してください。')
    dialog.ShowModal()

    file_path = dialog.GetPath()
    __, ext = os.path.splitext(file_path)

    if ext == ".jpg":
        histgram_main(file_path)