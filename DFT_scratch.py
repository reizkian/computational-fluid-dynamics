'''
D E P A R T E M E N   F I S I K A  U G M
===============================================================================
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : DFT_scratch
Created : 6 Maret 2019
Edited  : -
===============================================================================
'''

import numpy as np
import matplotlib.pyplot as plt

N=100
lamb=1
x=np.linspace(0,lamb,N)

def sin(A,n):
    return A*np.sin(2*np.pi*n*x/1)

y=sin(1,1)

img=(0+1.j)
dft_y=np.zeros(N,dtype=complex)

# Raw Discrete Fourier Transform, direct implementation
for i in range(0,N):
    for j in range(0,N):
        dft_y[i]=dft_y[i]+y[j]*np.exp(-img*2*np.pi*i*j/N) 
        
#Raw data, containing imaginary data
RAW_DFT=dft_y.copy()
FFT = np.fft.fft(y)

# Analytic Discrete Fourier Transform with Nyquiz=N/2
k=np.linspace(0,(N/2)-1,N/2)    #k space
dft1=np.sqrt(np.real(dft_y*np.conjugate(dft_y)))
Nyquiz=int(N/2)
dft2=dft1[:Nyquiz]/Nyquiz
ANALYTIC_DFT=dft2 #Processed data to form like analytic solution
    
# =============================================================================
# PLOT CODE
fig1 =  plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(x,y, 'b')
plt.title('Wave in X-space')
plt.grid(True)

fig2 =  plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(k,dft2, 'r')
plt.title('Fourier Transform (K-space)')
plt.grid(True) 
# =============================================================================
