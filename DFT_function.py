"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
===============================================================================
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : DFT_function
Created : Thu Mar 21 08:02:15 2019
==============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

N=100
lamb=1
x=np.linspace(0,lamb,N)
k=np.linspace(0,(N/2)-1,N/2)    #k space

def sin(A,n):
    return A*np.sin(2*np.pi*n*x/1)

y=sin(1,1)+sin(0.5,10)


#input_value to perform Discrete Fourier Transform
def dft_raw(input_value):
    import numpy as np
    img=(0+1.j)
    dft_y=np.zeros(N,dtype=complex)
    # Raw Discrete Fourier Transform, direct implementation
    for i in range(0,N):
        for j in range(0,N):
            dft_y[i]=dft_y[i]+y[j]*np.exp(-img*2*np.pi*i*j/N) 
    dft_done=dft_y
    return dft_done

rawdft=dft_raw(y) 

def dft_render(setdata):
    realvalue=np.sqrt(np.real(setdata*np.conjugate(setdata)))
    Nyquiz=int(N/2)
    dft_render=realvalue[:Nyquiz]/Nyquiz
    return dft_render

DFT=dft_render(rawdft)

# =============================================================================
# PLOT CODE
fig1 =  plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(x,y, 'b')
plt.title('Wave in X-space')
plt.grid(True)

fig2 =  plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(k,DFT, 'r')
plt.title('Fourier Transform (K-space)')
plt.grid(True) 
# =============================================================================
