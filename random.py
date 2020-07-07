"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
-------------------------------------------------------------------------------
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : 
Created : Sat Apr 27 22:26:42 2019
"""

import numpy as np
import matplotlib. pyplot as plt

N = 10**4
x = np.random.uniform(0,1,[N])
y = np.random.uniform(0,1,[N])

A = 0
B = 0
for i in range(N):
    r = np.sqrt(x[i]**2 + y[i]**2)
    if r<1:
        A=A+1
    else:
        B=B+1
pi = A*4/N

a = np.linspace(0,1,N)
b = np.sqrt(1-a**2)
m = (10-1)/(100-10000)
c= 10 - m*100
scaledot = m*N + c

plt.scatter(x,y,s=scaledot)
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(a,b, 'r')
plt.show()

print("==== M O N T E C A R L O ====")
print("random points = ",N)
print("include points = ",A)
print("exclude points = ",B)
print(" ")
print("-----------------------------")
print("Numerical ressult")
print("pi = ",pi)
