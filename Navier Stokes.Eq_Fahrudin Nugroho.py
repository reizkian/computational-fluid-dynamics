"""
D E P A R T E M E N   F I S I K A  -  U G M
Reizkian Yesaya_15/383192/PA/16852
email:reizkianyesaya@gmail.com
------------------------------------------------------------

Program : Navier Stokes.Eq_Fahrudin Nugroho 
Created : 12 November 2018
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def fungw(x,y):
	w1 = np.exp(-((x-np.pi+np.pi/5)**2 + (y-np.pi+np.pi/5)**2)/0.3)
	w2 = np.exp(-((x-np.pi+np.pi/5)**2 + (y-np.pi+np.pi/5)**2)/0.2)
	w3 = np.exp(-((x-np.pi+np.pi/5)**2 + (y-np.pi+np.pi/5)**2)/0.4)
	w=w1-w2+w3
	return w

myu = 0.01
eps = 0.1

N = 2**9
L = 40*np.pi
axis1 = np.linspace(-L/2,L/2,N)
x,y = np.meshgrid(axis1,axis1)

W = np.random.uniform(-1,1,[N,N])*0.01
W1 = np.fft.fft2(W)

h = 0.05
tmax = 100
nmax = np.round(tmax/h)
nplt = np.floor((tmax/500)/h)

k1 = np.arange(0,(N/2),1)
k2 = 0.0
k3 = np.arange(-((N/2)-1),0,1)
k11 = np.hstack((k1,k2))
k = np.hstack((k11,k3))
K1 = ((k*2*np.pi)/L).reshape(N,)
K = ((K1**2)).reshape(N,)
Kx,Ky = np.meshgrid(K,K)
K2 = (Kx**2 + Ky**2)

for l in np.nditer(K2, op_flags=['readwrite']):
	if l == 0.0:
		l[...] = 1

q = -myu*(K2)
c = np.exp(q*h)

c1 = np.zeros([N,N])
for i in range (N):
	for p in range(N):
		if q[i,p]==0:
			c1[i,p]=0.0
		else:
			c1[i,p]=((q[i,p]*h+1)*c[i,p]-1-2*h*q[i,p])/(h*(q[i,p]**2))

c2 = np.zeros([N,N])
for i in range (N):
	for p in range (N):
		if q[i,p]==0:
			c[i,p]=0.0
		else:
			c2[i,p] = (-c[i,p]+1+h*q[i,p])/(h*(q[i,p]**2))

fungf0 = np.zeros([N,N],dtype='D')
fungf1 = np.zeros([N,N],dtype='D')
fig, ax = plt.subplots()
data = []

img = []
for i in np.arange(1,nmax,1):
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
	W1 = A1
	fungf0 = fungf1
	fungf0 = fungf1
	if np.mod(i,nplt) == 0:
		data.append(val)
		Z = np.real(val)
		img.append([ax.imshow(Z)])
	if i/nplt == 10:
		print(Z)
	print(i/nplt)

#anim = animation.ArtistAnimation(fig, img, interval=200, blit=True, repeat_delay=10.0)
#plt.show() 		
				 
	
 