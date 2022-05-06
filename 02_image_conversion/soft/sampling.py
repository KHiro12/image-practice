import os

import cv2
import wx


def sampling_main(file_path):
    img = cv2.imread(file_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sampling_img = sampling_do(img_gray, 5)
    quantization_img = quantization_do(img_gray, 64)

    while True:
        cv2.imshow("Frame", img_gray)
        cv2.imshow("Frame_Sampling", sampling_img)
        cv2.imshow("Frame_Quantization", quantization_img)
        key = cv2.waitKey(30)
        # enterキーで
        # 閉じるようにしてみる
        if key == 13:
            break


def sampling_do(img, magnification):
    img_out = img.copy()

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            gaso_i = i - int(i % magnification)
            gaso_j = j - int(j % magnification)
            img_out[i][j] = img[gaso_i][gaso_j]

    return img_out


def quantization_do(img, step):
    img_out = img.copy()

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            quant = int(float(img[i][j]) / (float(step)+0.5)) * step
            quant = min(quant, 255)
            quant = max(quant, 0)
            img_out[i][j] = quant

    return img_out


if __name__ == "__main__":
    app = wx.App()
    dialog = wx.FileDialog(None, u'動画像を選択してください。')
    dialog.ShowModal()

    file_path = dialog.GetPath()
    __, ext = os.path.splitext(file_path)

    if ext == ".jpg":
        sampling_main(file_path)