# coding: utf-8

import tkinter
root = tkinter.Tk()

root.title("ウィンドウのタイトル")

cvs = tkinter.Canvas(width=500, height=500, bg="white")
cvs.pack()
cvs.create_line(0,0,500,300)
root.mainloop()
