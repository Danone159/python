import tkinter

canvas = tkinter.Canvas(width=600, height=450, bg='white')
canvas.pack()

xx, yy = 0, 0

def klik(event):
    global xx, yy
    x, y = event.x, event.y
    canvas.create_oval(x-5, y-5, x+5, y+5, fill='red')
    if xx >= 0:
        canvas.create_line(xx, yy, x, y)
    xx, yy = x, y

canvas.bind('<Button-1>', klik)
