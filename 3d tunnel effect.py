from tkinter import *
import time, math

t = Tk()
t.resizable(False, False)
c = Canvas(t, width=800, height=600, bg="#000000")
c.pack()

ticks = 1

rings = []
remove = []
for i in range(1, 25):
    rings.append(i)

def draw():
    for i in range(len(rings)):
        radius = 1000 / rings[i]
        col = int(255 - (rings[i] * 15))
        if col < 0:
            col = 0
        ccol = hex(col)[2:]
        ccol = (2 - len(ccol)) * "0" + ccol
        c.create_oval(400 - radius, 300 - radius, 400 + radius, 300 + radius, fill="#000000", outline="#00" + ccol + "00")
    
while True:
    time.sleep(0.1)
    c.delete("all")
    draw()
    ticks += 1
    if ticks == 10:
        ticks = 1
        rings.append(25)
    for i in range(len(rings)):
        rings[i] -= 0.1
        if rings[i] <= 0:
            remove.append(rings[i])
    for r in remove:
        rings.remove(r)
    remove = []
    c.update()
    t.update()
