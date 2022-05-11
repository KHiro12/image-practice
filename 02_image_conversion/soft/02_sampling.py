import os

import cv2
import matplotlib.pyplot as plt
import wx


# 画像出力
def output_img(img, title, file_name):
    fig = plt.figure()

    if len(img.shape) >= 3:
        # カラー用
        plt.imshow(img)
        plt.title(title)
        fig.savefig(os.path.join("output", file_name))
    else:
        # グレースケール用
        plt.imshow(img, vmin=0, vmax=255)
        plt.title(title)
        plt.gray()
        plt.colorbar()
        fig.savefig(os.path.join("output", file_name))


# 画像処理メイン
def img_process_main(file_path):
    # 画像の読み込み
    img = cv2.imread(file_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # RGB→グレースケール
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    # 画像描画
    output_img(img_rgb, "RGB", "00_rgb_img.jpg")
    output_img(img_gray, "GRAY", "01_gray_img.jpg")


# メイン関数
if __name__ == "__main__":
    # ファイルダイアログ作成
    app = wx.App()
    dialog = wx.FileDialog(None, u'画像を選択してください。')
    dialog.ShowModal()

    file_path = dialog.GetPath()
    __, ext = os.path.splitext(file_path)
    dialog.Destroy()

    # 出力フォルダ作成
    if not os.path.exists("output"):
        os.mkdir("output")

    if ext == ".jpg":
        img_process_main(file_path)
