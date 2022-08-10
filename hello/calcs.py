# In[]
from scipy.optimize import minimize

# In[]

def calc(amount, interest, period):

    R_monthly=1+interest/100/12
    P_monthly=period*12-1
    money=amount + \
        amount * R_monthly * \
        (R_monthly**P_monthly-1) / \
        (R_monthly-1)
    return money

#'{:,}'.format(math.floor(calc(12000,2.55,15)))

def func(x):
    x0=x[0]
    x1=x[1]
    chk_val=(calc(x0,x1,fulltime)-finalvalue)**2
    return chk_val

finalvalue=950000
fulltime=5
x0=[10000,1.0]
result = minimize(func,x0=x0,bounds=[(1,20000),(0,5)])
result
#result.x
# %%
