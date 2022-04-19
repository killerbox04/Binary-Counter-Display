#8-Bit Blinking Lights
#la locura está aquí

from tkinter import *
import tkinter as ttk
import time

global R8X
global R4X
global R2X
global R1X
global clk

off = "pink"
on = "Red"
stanDelay = time.sleep(1)
clk = 1

def Halt():
    global after_id

def update():
    global after_id
    global clk 
    clk += 1
    if clk % 1 == 0:
        if mainCan.itemcget(R1X, "fill") == "pink":
            mainCan.itemconfig(R1X, fill = "red")
        else:
            mainCan.itemconfig(R1X, fill = "pink")

    if clk % 2 == 0:
        if mainCan.itemcget(R2X, "fill") == "pink":
            mainCan.itemconfig(R2X, fill = "red")
        else:
            mainCan.itemconfig(R2X, fill = "pink")

    if clk % 4 == 0:
        if mainCan.itemcget(R4X, "fill") == "pink":
            mainCan.itemconfig(R4X, fill = "red")
        else:
            mainCan.itemconfig(R4X, fill = "pink")

    if clk % 8 == 0:
        if mainCan.itemcget(R8X, "fill") == "pink":
            mainCan.itemconfig(R8X, fill = "red")
        else: mainCan.itemconfig(R8X, fill = "pink") 
    

    after_id = master.after(1000, update)

def Start():
    update()

def Halt():
    global after_id
    
    if after_id:
        master.after_cancel(after_id)

master = ttk.Tk()

master.geometry("600x100")
master.resizable(width = False, height = False)

mainCan = Canvas(master, width=400, height=100)


# a, b, c, d | a = start x pos, b = start y pos, c = end x pos, d = end y pos 

R8X = mainCan.create_rectangle(
    0, 0, 100, 100,
    fill = "pink"
)

R4X = mainCan.create_rectangle(
    100, 0, 200, 200,
    fill = "pink"
)

R2X = mainCan.create_rectangle(
    200, 0, 300, 300,
    fill = "pink"
)

R1X = mainCan.create_rectangle(
    300, 0, 400, 400,
    fill = "pink"
)


master.grid

mainCan.grid(
    row = 0,
    column = 0,
    sticky = "NSEW"
)

startButton = ttk.Button(
    master,
    text = "Start",
    command = update
)

stopButton = ttk.Button(
    master,
    text = "Stop",
    command = Halt
)

startButton.grid(
    row = 0,
    column = 1
)

stopButton.grid(
    row = 0,
    column = 2
)



master.mainloop()



