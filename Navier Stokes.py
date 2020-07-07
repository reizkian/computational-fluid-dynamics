"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
===============================================================================
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : Navier Stokes
Created : Tue Mar 26 15:23:30 2019
==============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

#Numerical properties
L=1                                     # system size
N=1000                                  # discritization
x=np.linspace(0,L,N+1)                  # physical space x-coordinate
dk=np.pi/L
k_plus=np.arange(1,N/2+2,1)             # fourier k-space
k_minus=np.arange(-N/2+1,0,1)
k_array=np.hstack((k_plus,k_minus))
k=k_array*dk
k2=k**2                                         
img=(0+1.j)                             #imaginary number



#P H I S I C A L   P R O P E R T I E S
# =====================================
nu=0.01                # kinematic viscousity
rho=1                   # fluid density
pressure=np.zeros(N+1)  # Pressure Field
u0=1/(np.cosh(10.0*x)**2)        # Initial Velocity (along x-axis)
# =====================================



def df_dx(y): #diferentiating function
    dfdx=np.zeros(N+1)
    for i in range(0,N+1):
        if i <= N-1:
            dfdx[i] = (y[i+1]-y[i])/(L/N)
        if i == N:
            dfdx[i]=dfdx[i-1]
    return dfdx


#E T D   H A N D L I N G
# =====================================
u0_hat=np.fft.fft(u0)
A=u0_hat.copy()
U2=u0**2
U2_fft=np.fft.fft(U2)
dP_dx=df_dx(pressure)
fftdpdx=np.fft.fft(dP_dx)

tmax=1
N_t=100
dt=tmax/N_t

#MONITOR ARRAY
Fn_monitor=np.zeros(N,dtype=complex)
ech_monitor=np.zeros(N,dtype=complex)
for t in range(0,N_t):
    for i in range (0,N):
        ech=np.exp(-k2[i]*nu*(t*dt))
        Fn=-(1/rho)*dP_dx[i]+(img*k[i]*U2_fft[i]/2)
        ech_monitor[i]=ech
        Fn_monitor[i]=Fn
        A[i]=A[i]*ech+Fn*(ech-1)/(-k2[i]*nu)
#Numerical Result u(t)
uT=np.real(np.fft.ifft(A))        



   
# =============================================================================
# PLOT CODE
fig1 =  plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(x,uT,'r')
plt.title('uT')
plt.grid(True) 

fig2 =  plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(x,u0,'b')
plt.title('u0')
plt.grid(True) 
# =============================================================================
