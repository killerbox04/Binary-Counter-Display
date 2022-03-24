#Update
import json
import time

global clk 

X1 = 0
X2 = 0
X4 = 0
X8 = 0
clk = 0


testlist = 1, 2, 4, 8


def update(Uclk):

    if Uclk % 1 == 0:
        flip(X1)
        if Uclk
    if Uclk % 2 == 0:
        flip(X2)
    if Uclk % 4 == 0:
        flip(X4)
    if Uclk % 8 == 0:
        flip(X8)

    return(X8, X4, X2, X1)


def flip(val):
    if val == 0:
        newVal = 1

    elif val == 1:
        newVal = 0

    return newVal
    
