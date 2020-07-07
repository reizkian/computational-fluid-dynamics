"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
-------------------------------------------------------------------------------
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : Vortricity
Created : Mon Apr 22 08:08:21 2019
"""

import numpy as np
import mayavi.mlab as mlab
import matplotlib.pyplot as plt

Ngrid = 2**9
vsc = 0.005
myu = 0.0001
eps = 0.1

q = 2 * np.pi / Ngrid
L = 1
axis = q * np.arange( 0, Ngrid, 1 )
x , y = np.mgrid[0:Ngrid,0:Ngrid] * q
h = 0.001
tmax = 0.01
nmax = np.round(tmax/h)
interval= h*tmax

# Initial value votricity
w1 = np.exp(-((x-np.pi+np.pi/5)**2 + (y-np.pi+np.pi/5)**2)/0.3)
w2 = np.exp(-((x-np.pi-np.pi/5)**2 + (y-np.pi+np.pi/5)**2)/0.2)
w3 = np.exp(-((x-np.pi-np.pi/5)**2 + (y-np.pi-np.pi/5)**2)/0.4)
omega = w1 - w2 + w3

W = np.random.uniform(-1,1,[Ngrid,Ngrid])*0.01
omegar=omega+W
W1 = np.fft.fft2(omega)

# k-space construction
k1 = np.arange(1,(Ngrid/2+1),1)
k3 = np.arange(-((Ngrid/2)),0,1)
k = np.hstack((k1,k3))
K1 = ((k*2*np.pi)/L).reshape(Ngrid,)
K = ((K1**2)).reshape(Ngrid,)
Kx , Ky = np.meshgrid(K,K)
K2 = (Kx**2 + Ky**2)

q = -myu*(K2)
c = np.exp(q*h)

c1 = np.zeros([Ngrid,Ngrid])
for i in range (Ngrid):
	for p in range(Ngrid):
		if q[i,p]==0:
			c1[i,p]=0.0
		else:
			c1[i,p]=((q[i,p]*h+1)*c[i,p]-1-2*h*q[i,p])/(h*(q[i,p]**2))

c2 = np.zeros([Ngrid,Ngrid])
for i in range (Ngrid):
	for p in range (Ngrid):
		if q[i,p]==0:
			c[i,p]=0.0
		else:
			c2[i,p] = (-c[i,p]+1+h*q[i,p])/(h*(q[i,p]**2))
            
fungf0 = np.zeros([Ngrid,Ngrid],dtype='D')
fungf1 = np.zeros([Ngrid,Ngrid],dtype='D')

plt.imshow(omega, cmap='jet')
plt.show()

for i in np.arange(0,100,10):
    psi_hat = -W1/K2
    u = np.real(np.fft.ifft2(Ky*psi_hat))
    v = np.real(np.fft.ifft2(-Kx*psi_hat))
    w_x = np.real(np.fft.ifft2(Kx*W1))
    w_y = np.real(np.fft.ifft2(Ky*W1))
    Vgrad = u*w_x + v*w_y
    Vgrad_hat = np.fft.fft2(Vgrad)
    fungf1 = 1j*(Ky*Vgrad_hat+(-Kx)*Vgrad_hat)
    A1 = W1*c +fungf1*c1 + fungf0*c2
    val = np.real(np.fft.ifft2(A1)) 
    fungf0 = fungf1
    
    print("TIME = ", i*h," sec")
    plt.imshow(val, cmap='jet')
    plt.show()
    
    