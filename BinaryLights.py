#8-Bit Blinking Lights
#la locura está aquí

from base64 import standard_b64decode
import json
from json.tool import main
from textwrap import fill
from tkinter import *
import tkinter as ttk
import time
import Update

global R8X
global R4X
global R2X
global R1X

off = "pink"
on = "Red"
stanDelay = time.sleep(1)
clk = 0


def start():
    Update.update()

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
    text = "Iterate",
    command = start
)

startButton.grid(
    row = 0,
    column = 1
)

master.mainloop()
