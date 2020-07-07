"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
===============================================================================
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : Method
Created : Wed Mar 20 22:23:51 2019
==============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

N=2**10
L=2
nu=0.001
x=np.linspace(-L/2,L/2,N)

dk=np.pi/L
k_plus=np.arange(0,N/2+1,1)
k_minus=np.arange(-N/2+1,0,1)
k_array=np.hstack((k_plus,k_minus))
k=k_array*dk
k2=k**2

u0=1/(np.cosh(10.0*x)**2)
u0_hat=np.fft.fft(u0)
A=u0_hat.copy()

tmax=3
N_t=100
dt=tmax/N_t
for t in range(0,N_t,10):
    for i in range (0,N):
        A[i]=A[i]*np.exp(-k2[i]*nu*(t*dt))

    uT=np.real(np.fft.ifft(A))
    
    
plt.plot(x,u0,'b', label='t=0')
plt.plot(x,uT,'r', label='t=5')
plt.grid()
plt.xlabel('position')
plt.ylabel('Temperature')
plt.title('TEMPERATURE DIFUSE')
plt.grid(True)
plt.legend()
plt.show()