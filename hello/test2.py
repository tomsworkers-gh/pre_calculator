"""
検証用に勝手に作ったファイルなので
いずれ消す
"""

# In[]

import math
from scipy.optimize import minimize
import calcs

def func(x):
    x0=x[0]
    chk_val=(calcs.calc(monthly,x0,fulltime)-finalvalue)**2
    return chk_val

finalvalue=950000
fulltime=5
monthly=16000
x0=[1.0]
if finalvalue<monthly*12*fulltime:
    print("減っています")
else:
    result = minimize(func,x0=x0,bounds=[(0.00001,100)])
    print("年利",math.floor(result.x[0]*10000)/10000,"%で運用")
# %%
