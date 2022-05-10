import os

import cv2
import wx


# RGB分解
def color_separate(img):
    r_img = img[:, :, 2]
    g_img = img[:, :, 1]
    b_img = img[:, :, 0]

    return r_img, g_img, b_img

# 画像処理メイン
def img_process_main(file_path):
    # 画像の読み込み
    img = cv2.imread(file_path)

    # RGB→グレースケール
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # RGB分解
    r_img, g_img, b_img = color_separate(img)

    while True:
        # 画像の描画
        cv2.imshow("RGB", img)
        cv2.imshow("GRAY", img_gray)
        cv2.imshow("R", r_img)
        cv2.imshow("G", g_img)
        cv2.imshow("B", b_img)

        key = cv2.waitKey(30)
        # enterキーで
        # 閉じるようにしてみる
        if key == 13:
            break


# メイン関数
def main():
    # ファイルダイアログ作成
    app = wx.App()
    dialog = wx.FileDialog(None, u'画像を選択してください。')
    dialog.ShowModal()

    file_path = dialog.GetPath()
    __, ext = os.path.splitext(file_path)

    if ext == ".jpg":
        img_process_main(file_path)


if __name__ == "__main__":
    # メイン関数呼び出し
    main()