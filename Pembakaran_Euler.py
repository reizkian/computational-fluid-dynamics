"""
D E P A R T E M E N   F I S I K A
Reizkian Yesaya_15/383192/PA/16852
program: Pembakaran_Euler Method
created: 31 Juli 2018
"""
import numpy as np
import matplotlib.pyplot as plt

def area(u,t):
    area=4*np.pi*(u**2)
    return area

def volume(u,t):
    volume=(4*np.pi*(u**3))/3
    return volume

def du_dt(u,t):
    du_dt=(area(u,t)-volume(u,t))
    return du_dt


u0=0.05
t0=0
h=0.02

u=[]
t=[]
A=[]
V=[]

if t0<10:    
    while t0<=2:
        u_tp1=u0+h*du_dt(u0,t0)
        u0=u_tp1
        u.append(u0)
        t0=t0+h
        t.append(t0)
        
        v=volume(u0,t)
        a=area(u0,t)
        V.append(v)
        A.append(a)
print(t0,"   ",u0)
    
plt.grid(True)
plt.plot(t,u,'g--')
#plt.plot(t,V,'r--')
#plt.plot(t,A,'b--')
plt.show
