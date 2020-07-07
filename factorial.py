"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
-------------------------------------------------------------------------------
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : Taylor
Created : Fri May  3 17:18:56 2019
"""

import numpy as np
import matplotlib.pyplot as plt

N=100

def factorial(n):
    f=1
    for i in range(1,n):
       f=f*(i+1)
    return f

x = np.linspace(0,2*np.pi,N)
y = np.sin(x)

   
sums=np.zeros(N)

for i in range(50):
    a=(-1)**i*((x)**(2*i+1))/factorial(2*i+1)
    sums=sums+a

z = sums
        
plt.plot(x,y,'b')
plt.plot(x,z,'r--')
plt.grid(True)
plt.show()