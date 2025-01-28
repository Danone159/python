import tkinter
import random
canvas=tkinter.Canvas()
canvas.pack()

def kresli():
    x=random.randrange(600)
    y=random.randrange(450)
    canvas.create_oval(x-10, y-10, x+10, y+10, fill='blue')
    canvas.after(100,kresli)



def kresli1():
    x=random.randrange(500)
    y=random.randrange(300)
    canvas.create_oval(x-10, y-10, x+10, y+10, fill='red')
    canvas.after(200,kresli1)


kresli()
kresli1()
