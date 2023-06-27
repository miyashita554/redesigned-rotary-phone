# tkinterはpythonのGUI(グラフィカルユーザーインタフェース)
# ウィンドウとかボタンとかを画面に出して操作できるようにするプログラム
import tkinter

# ウィンドウ作成
root = tkinter.Tk()
root.title("勇者求む！")
root.minsize(640.480)
root.option_add("*foot",("メイリオ",14))

# 画像読み込み
img1 = tkinter.PhotoImage(file = 'img4/chap4-1-1.png')
img1 = tkinter.PhotoImage(file = 'img4/chap4-1-2.png')
img1 = tkinter.PhotoImage(file = 'img4/chap4-1-3.png')

# キャンパス作成
canvas = tkinter