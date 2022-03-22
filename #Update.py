#Update
import json
import time

global X1
global X2
global X4
global X8

X1 = 0
X2 = 0
X4 = 0
X8 = 0


testRange = range(1,17)
testlist = 1, 2, 4, 8


def update(clk):
    global X1
    global X2
    global X4
    global X8

    for val in testlist:
        if clk % val == 0:
            if val == 1:
                X1 = flip(X1)
            if val == 2:
                X2 = flip(X2)
            if val == 4:
                X4 = flip(X4)
            if val == 8:
                X8 = flip(X8)    
        
        return(X1, X2, X4, X8)


def flip(val):
    if val == 0:
        newVal = 1

    elif val == 1:
        newVal = 0

    return newVal


for val in testRange:
    pval = update(val)
    print(pval)
    time.sleep(1)