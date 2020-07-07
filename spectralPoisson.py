"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
-------------------------------------------------------------------------------
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : spectralPoisson
Created : Sun May 26 23:18:29 2019
"""

import numpy as np
import matplotlib.pyplot as plt
import mayavi.mlab as mlab

N=51
L=1
dx=L/(N-1)
dy=L/(N-1)
dt=0.001

axes = np.linspace(-1,1,N)
X , Y = np.meshgrid(axes,axes)
X=X.T
Y=Y.T

P = np.zeros([N,N],dtype=complex)
b = np.zeros([N,N],dtype=complex)
b[int(N/2),int(N/2)] = -100

k_plus = np.arange(1,N/2+1,1)
k_minus = np.arange(-(N-1)/2,0,1)
k = np.hstack((k_plus,k_minus))
Kx , Ky = np.meshgrid(k,k)
kx = Kx.T
ky = Ky.T

def FD():
    for t in range(100):
        print(t)
        for i in range(1,N-1):
            for j in range(1,N-1):
                a1 = (dy**2)*(P[i+1,j]+P[i-1,j])
                a2 = (dx**2)*(P[i,j+1]+P[i,j-1])
                a3 = (dx**2)*(dy**2)*(b[i,j])
                P[i,j] = (a1+a2-a3)/2/(dx**2+dy**2)
                
    mlab.clf()
    mlab.surf(X,Y,np.real(P), warp_scale="auto")
    mlab.outline()
    mlab.axes()
    
    return np.real(P)
def spectral():
    P_fft = np.fft.fft2(P)
    b_fft = np.fft.fft2(b)
    for t in range(10):
        print(t)
        P_fft= -b_fft/(kx**2+ky**2)
    
    P_spectral = np.real(np.fft.ifft2(P_fft))
    mlab.clf()
    mlab.surf(X,Y,P_spectral, warp_scale="auto")
    mlab.outline()
    mlab.axes()
    
    return P_spectral

spectral()