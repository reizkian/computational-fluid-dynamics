"""
D E P A R T E M E N   F I S I K A  -  U G M
Reizkian Yesaya_15/383192/PA/16852
email:reizkianyesaya@gmail.com
------------------------------------------------------------

Program : Heat.eq_Spectral
Created : 17 November 2018
"""
import numpy as np
import matplotlib.pyplot as plt

l=1
N=256
dx=l/N
x_array=np.arange(1-N/2,N/2+1,1)
x=x_array*dx
xp=np.linspace(-1,1,N)

nu=0.01
T=5
dk=np.pi/l
k_plus=np.arange(0,129,1)
k_minus=np.arange(-127,0,1)
k_array=np.hstack((k_plus,k_minus))
k=k_array*dk
k2=k**2

u0=1/(np.cosh(10.0*x)**2)
u0_hat=np.fft.fft(u0)
uT=np.real(np.fft.ifft(np.exp(-nu*k2*T)*u0_hat))

#mask=x<0
plt.plot(xp,uT)
plt.grid(True)