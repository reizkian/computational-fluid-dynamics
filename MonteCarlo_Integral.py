"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
-------------------------------------------------------------------------------
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : Montecarlo_pi
Created : Sat Apr 27 22:26:42 2019
"""

import numpy as np
import matplotlib. pyplot as plt
import time 
time_start = time.time()

N = 10**4   #data size
x = np.random.uniform(0,1,[N])
y = np.random.uniform(0,1,[N])
A = 0 # storing variable
B = 0 # storing variable
for i in range(N):
    f=x[i]**2
    if y[i]<=f:
        A=A+1
    else:
        B=B+1
    
L = A/N  # Numerical result

# PLot Construction 
a = np.linspace(0,1,N)
b = a**2
plt.scatter(x,y,s=0.1)
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(a,b, 'r')
plt.show()
print("======= M O N T E C A R L O =======")
print("random points = ",N)
print("include points = ",A)
print("exclude points = ",B)
print(" ")
print("-----------------------------")
print("Numerical ressult")
print("Integral Kurva = ",L)
print("-----------------------------")
time_stop = time.time()
time_exe = time_stop-time_start
minute = time_exe/60
print(" ")
print("program executed normaly")
print("running time = ",time_exe,"sec"," (",minute," minute",")")
