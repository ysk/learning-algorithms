# coding: utf-8

import tkinter
root = tkinter.Tk()

root.title("軸とメモリを描く")

cvs = tkinter.Canvas(width=600, height=600, bg="white")
cvs.pack()

ox = 300
oy = 300

cvs.create_text(ox+20, oy+15, text="(0,0)")

#Y軸を描く
cvs.create_line(ox, 0, ox, 600, fill="gray")
#Y軸のメモリ
for y in range(0, 600, 10):
    cvs.create_line(ox-2, y, oy+3, y, fill="silver")

#X軸を描く
cvs.create_line(0, oy, 600, oy, fill="gray")
#X軸のメモリ
for x in range(0, 600, 10):
    cvs.create_line(x, oy-2, x, oy+3, fill="silver")

root.mainloop()
