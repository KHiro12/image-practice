import os

import cv2
import wx


def calor_img_main(file_path):
    img = cv2.imread(file_path)
    r_img,g_img,b_img = rgb_separate(img)
    cv2.imwrite("r.jpg", r_img)
    cv2.imwrite("g.jpg", g_img)
    cv2.imwrite("b.jpg", b_img)

    while True:
        cv2.imshow("Frame", img)
        cv2.imshow("Frame_R", r_img)
        cv2.imshow("Frame_G", g_img)
        cv2.imshow("Frame_B", b_img)
        key = cv2.waitKey(30)
        # enterキーで
        # 閉じるようにしてみる
        if key == 13:
            break


def rgb_separate(img):
    img_r = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_g = img_r.copy()
    img_b = img_r.copy()

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_r[i][j] = img[i][j][2]
            img_g[i][j] = img[i][j][1]
            img_b[i][j] = img[i][j][0]

    return img_r, img_g, img_b


if __name__ == "__main__":
    app = wx.App()
    dialog = wx.FileDialog(None, u'動画像を選択してください。')
    dialog.ShowModal()

    file_path = dialog.GetPath()
    __, ext = os.path.splitext(file_path)

    if ext == ".jpg":
        calor_img_main(file_path)