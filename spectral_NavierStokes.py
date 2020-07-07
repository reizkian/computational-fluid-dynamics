"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
-------------------------------------------------------------------------------
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : spectral_NavierStokes
Created : Mon May 20 14:07:45 2019
"""

import numpy as np
import matplotlib.pyplot as plt
import mayavi.mlab as mlab

#Parameter Numerik
N=51
L=1
dx = L/(N-1)
dy = L/(N-1)
dt = 0.001

#Parameter Fisis
N_time = 100        # untuk menghitung 1 detik
N_ptime = 50       # step-time untuk tekanan
vis = 0.1           # viskositas kinematik
rho = 1             # massa jenis
nu = vis/rho

#Deklarasi Variabel Ruang
axes1 = np.linspace(0,L,N)
axes2 = np.linspace(-L,0,N)
x,y = np.meshgrid(axes1,axes1)

#Deklarasi Variabel k-space
k_plus = np.arange(1,N/2+1,1)
k_minus = np.arange(-(N-1)/2,0,1)
k = np.hstack((k_plus,k_minus))
Kx , Ky = np.meshgrid(k,k) 

u = np.zeros([N,N]) #kecepatan arah-x
v = np.zeros([N,N]) #kecepatan arah-y
P = np.zeros([N,N]) #Tekanan
b = np.zeros([N,N]) #source Tekanan

u[:,-1] = 1 #Syarat Batas, u=1 pada y=1

# Mulai Iterasi
#------------------------------------------------------------------------------
for n in range(N_time):
    percentage = n*100/N_time
    print("RUNNIG =",percentage, "%")
    
    un = u.copy()
    vn = v.copy()
    
    u_fft = np.fft.fft2(un)
    v_fft = np.fft.fft2(vn)
    P_fft = np.fft.fft2(P)
    b_fft = np.fft.fft2(b)
    
    u_xfft = u_fft*Kx*1j
    u_yfft = u_fft*Ky*1j
    v_xfft = v_fft*Kx*1j
    v_yfft = v_fft*Ky*1j
    
    u_x = np.real(np.fft.ifft2(u_xfft))
    u_y = np.real(np.fft.ifft2(u_yfft))
    v_x = np.real(np.fft.ifft2(v_xfft))
    v_y = np.real(np.fft.ifft2(v_yfft))
    
    b1 = u_x*u_x
    b2 = v_y*v_y
    b3 = 2*u_y*v_x
    b_fft = rho*np.fft.fft2(u_x+v_y)/dt - rho*np.fft.fft2(b1+b2+b3)
    b=np.real(np.fft.ifft2(b_fft))
    
    for t in range(N_ptime):
        P_fft= -b_fft/(Kx**2+Ky**2)
    
    P = np.real(np.fft.ifft2(P_fft))
    #Syarat Batas Tekanan
    P[:,0]  = P[:,1]    # dP/dy = 0  pada y = 0
    P[:,-1] = 0	        # P = 0      pada y = 2
    P[0,:]  = P[1,:]    # dP/dx = 0  pada x = 0
    P[-1,:] = P[-2,:]   # dP/dx = 0  pada x = 1    
    
    P_xfft = P_fft*Kx*1j
    P_yfft = P_fft*Ky*1j
    
    advection_ux = un*u_xfft
    advection_uy = vn*u_yfft
    advection_vx = un*v_xfft
    advection_vy = vn*v_yfft
    
    Fnu = - advection_ux - advection_uy - P_xfft/rho
    Fnv = - advection_vx - advection_vy - P_yfft/rho
    
    c = vis*(Kx**2+Ky**2)
    ech = np.exp(c*dt)
    
    ui = un*ech + Fnu*(ech-1)/c
    vi = un*ech + Fnv*(ech-1)/c
    
    u=np.real(np.fft.ifft(ui))
    v=np.real(np.fft.ifft(vi))
    
    u[:,-1] = 1  #u(x,y=1) = 1
    u[:,0]  = 0  #u(x,y=0) = 0
    u[0,:]  = 0  #u(x=0,y) = 0
    u[-1,:] = 0  #u(x=1,y) = 0
    
    v[:,-1] = 0  #u(x,y=1) = 0
    v[:,0]  = 0  #u(x,y=0) = 0
    v[0,:]  = 0  #u(x=0,y) = 0
    v[-1,:] = 0  #u(x=1,y) = 0
    
#CODE untuk plot
U=u.T
V=v.T
Pn=P.T

VelocityMagnitude = np.sqrt(U**2+V**2)

#Constructing Plot
total_time = N_time*dt
colorMagnitude = "jet"
colorPressure = "seismic"
titleVelocity = "MAGNITUDE KECEPATAN" " (t= 1 s)"
titlePressure = "MEDAN SKALAR TEKANAN" " (t= 1 s)"

fig1 =  plt.figure()
plt.pcolor(x,y,VelocityMagnitude, cmap=colorMagnitude)
plt.colorbar()
plt.quiver(x,y,U,V)
plt.xlabel("x")
plt.ylabel("y")
plt.title(titleVelocity )
plt.show()

fig2 =  plt.figure()
plt.pcolor(x,y,VelocityMagnitude, cmap=colorMagnitude)
plt.colorbar()
plt.streamplot(x,y,U,V, color='k')
plt.xlabel("x")
plt.ylabel("y")
plt.title(titleVelocity)
plt.show()

fig3 =  plt.figure()
plt.pcolor(x,y,Pn, cmap=colorPressure)
plt.colorbar()
plt.quiver(x,y,U,V)
plt.xlabel("x")
plt.ylabel("y")
plt.title(titlePressure)
plt.show()

fig4 =  plt.figure()
plt.pcolor(x,y,Pn, cmap=colorPressure)
plt.colorbar()
plt.streamplot(x,y,U,V, color='k')
plt.xlabel("x")
plt.ylabel("y")
plt.title(titlePressure)
plt.show()