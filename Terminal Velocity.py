"""
D E P A R T E M E N   F I S I K A
Reizkian Yesaya_15/383192/PA/16852
program: Euler Method_practice
created: 31 Juli 2018
"""

import numpy as np
import matplotlib.pyplot as plt

def differential(v,t):
    g= 9.8 #m/s**2
    k=0.05
    m=0.1 #kg
    
    dv_dt=g-(k*v/m)
    return dv_dt

"variable definition_constant"
h=0.1     #performance
v_0=0     #initial value x_0
t_0=0     #initial value y_0
"variable definition_list"
v=[]
t=[]
dv_dt=[]

v_aa=differential(v_0,t_0)*h+v_0
delta=v_aa-v_0

while delta>0.0001:
    print(v_0,"     ",t_0)
    v_ii=differential(v_0,t_0)*h+v_0
    
    delta=v_ii-v_0
    
    v_0=v_ii
    t_0=t_0+h
    
    v.append(v_0)
    t.append(t_0)
    dv_dt.append(differential(v_0,t_0))
 
    
plt.title('Euler Method')
plt.grid(True)
plt.plot(t,v,'bo-')
#plt.plot(x,dy_dx,'g--')
plt.show()

h=0.5*9.8*(t_0**2)

print("TERMINAL VELOCITY = ",v_0," m/s")
print("Ketinggian untuk mencapai TERMINAL VELOCITY adalah...")
print(h/1000,"km")