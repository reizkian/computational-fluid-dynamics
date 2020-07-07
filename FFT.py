"""
D E P A R T E M E N   F I S I K A  -  U G M
Reizkian Yesaya_15/383192/PA/16852
email:reizkianyesaya@gmail.com
------------------------------------------------------------

Program : FFT
Created : 20 November 2018
"""

import numpy as np
import matplotlib.pyplot as plt

n=100
x=np.linspace(0,10,n)
L=10
omega=2*np.pi/L
omg=x*omega

y1=2*np.sin(omega*x*30)
y2=np.sin(omega*x*10)
y=y1+y2

freq=np.fft.fftfreq(n)
mask=freq < 0

fft_y=np.absolute(np.fft.fft(y)/n)*2

plt.plot(omg[mask],fft_y[mask])
#plt.plot(x,y)
plt.grid(True)
plt.show()

