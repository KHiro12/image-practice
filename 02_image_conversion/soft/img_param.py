import os

import cv2
import wx


def param_main(file_path):
    img = cv2.imread(file_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    average = calc_average(img_gray)
    std = calc_std(img_gray, average)


    print(average)
    print(std)

    while True:
        cv2.imshow("Frame", img)
        key = cv2.waitKey(30)
        # enterキーで
        # 閉じるようにしてみる
        if key == 13:
            break


def calc_average(img):
    sum = 0
    count = 0

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            sum += img[i][j]
            count += 1

    if count != 0:
        return float(sum/count)
    else:
        return 0.0


def calc_std(img, average):
    sum = 0
    count = 0

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            diff = (float(img[i][j]) - average) ** 2
            sum += diff
            count += 1

    if count != 0:
        return float(sum/count)
    else:
        return 0.0


if __name__ == "__main__":
    app = wx.App()
    dialog = wx.FileDialog(None, u'動画像を選択してください。')
    dialog.ShowModal()

    file_path = dialog.GetPath()
    __, ext = os.path.splitext(file_path)

    if ext == ".jpg":
        param_main(file_path)