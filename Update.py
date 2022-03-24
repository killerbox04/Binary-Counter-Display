#Update
import json
import time
import BinaryLights



def update(X8, X4, X2, X1, clk):
    if clk % 1 == 0:    #If the remainder of clk divided by 1 is equal to zero
        if X1 == 0:     #If the value of X1 is 0
            X1U = 1      #Make its value 1

        elif X1 == 1:   #If the value of X1 is 1
            X1U = 0      #Make its value 0
    
    if clk % 2 == 0:    #If the remainder of clk divided by 2 is equal to zero
        if X2 == 0:     #If the value of X2 is 0
            X2U = 1      #Make its value 1

        elif X2 == 1:   #If the value of X2 is 1
            X2U = 0      #Make its value 0
    
    if clk % 4 == 0:    #If the remainder of clk divided by 4 is equal to zero
        if X4 == 0:     #If the value of X4 is 0
            X4U = 1      #Make its value 1

        elif X4 == 1:   #If the value of X4 is 1 
            X4U = 0      #Make its value 0

    if clk % 8 == 0:    #If the remainder of clk divided by 8 is equal to zero
        if X8 == 0:     #If the value of X8 is 0
            X8U = 1      #Make its value 1

        elif X8 == 1:   #If the value of X8 is 1 
            X8U = 0     #Make its value 0

    return(X8U, X4U, X2U, X1U)


