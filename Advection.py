"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
-------------------------------------------------------------------------------
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : Advection
Created : Wed Apr 24 22:23:10 2019
"""
import numpy as np
import mayavi.mlab as mlab
import matplotlib.pyplot as plt

N=2**9
L=1
#dt=0.01
img=(0+1.j)
x = np.linspace(-L,L,N)

u=0.02
d=0
nu=0.001

f=np.zeros(N)
for i in range(int(N/2-50),int(N/2+50)):
    f[i]=1


f = 1/(np.cosh(10.0*x)**2)
f_hat = np.fft.fft(f)

# k-space construction
k_plus=np.arange(0,N/2+1,1)
k_minus=np.arange(-N/2,0,1)
k_array=np.hstack((k_plus,k_minus))

dk=np.pi/L
k=k_array*dk
k2=k**2

tmax=10
N_t=100
dt=tmax/N_t

plt.plot(x,f)
for t in range(0,N_t,10):
    for i in range (0,N):
        c = (img*k[i]*u)-(k2[i]*d)
        f_hat[i]=f_hat[i]*np.exp(c*(t*dt))

    f_xt=np.real(np.fft.ifft(f_hat))

    time=dt*t
    print("time = ",time," sec")
    plt.plot(x,f_xt)
    plt.grid(True)
    plt.show()

print("=== PROGRAM HAS BEEN SUCESSFULLY EXECUTED ===")

# =============================================================================
# fig1 =  plt.figure()
# ax1 = fig1.add_subplot(111)
# ax1.plot(k_array,f_fft,'r')
# plt.title('')
# plt.grid(True) 
# 
# fig2 =  plt.figure()
# ax2 = fig2.add_subplot(111)
# ax2.plot(x,f,'b')
# plt.title('')
# plt.grid(True) 
# =============================================================================
