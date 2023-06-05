#Function to calculate the future values on assets
import numpy as np
def vp(vf,r,n):
    value = vf/(1+r)**n
    
#Function to calculate the net present value on assets
def pvn(rate, values):
    invest = np.npv(rate=rate, values=values)
    return invest