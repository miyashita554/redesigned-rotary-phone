import tkinter

root = tkinter.Tk()
root.title("リリーに質問")
root.minsize(640, 480)
root.option_add("*font", ["MS Pゴシック",22])

canvas = tkinter.Canvas(bg="black" , width=640 , height=480)
canvas.place(x=0,y=0)
img = tkinter.PhotoImage(file="img3/chap3-back.png")
canvas.create_image(320,240,image=img)

question = tkinter.Label(text="知りたいのは何分かな？",bg="white")
question.place(x=100,y=40)

entry = tkinter.Entry(width=12, bd=4)
entry.place(x=50,y=133)

askbutton = tkinter.Button(text="聞く")
askbutton.place(x=260,y=125)

answer = tkinter.Label(text="・・・・・・・・",bg="white")
answer.place(x=115,y=235)

def ask_click():
    val = entry.get()
    minutes = float(val)
    hours = round(minutes/60, 2)
    answer["text"] = str(hours) +"時間だね！"

askbutton["command"] = ask_click    

root.mainloop()

