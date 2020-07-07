"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
-------------------------------------------------------------------------------
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program :Poisson
Created : Mon May 13 16:08:54 2019
"""
import numpy as np
import mayavi.mlab as mlab

time = 100
N = 51
La=0
Lb=1
axes = np.linspace(La,Lb,N)
x , y = np.meshgrid(axes,axes)

X=x.T
Y=y.T

dx = abs(La-Lb)/(N-1) 
dy = abs(La-Lb)/(N-1)

u = np.zeros([N,N])
b = np.zeros([N,N])

b[int(N/2),:] = -100
b[:,int(N/2)] = -100

for t in range (time):
    print(t)
    for i in range (1,N-1):
        for j in range (1,N-1):
            u_xx = (u[i+1,j]+u[i-1,j]) * (dy**2)
            u_yy = (u[i,j+1]+u[i,j-1]) * (dx**2)
            u[i,j] = ( u_xx + u_yy - b[i,j]*(dx**2)*(dy**2) ) / ((dx**2)+(dy**2)) /2

mlab.clf()
mlab.surf(X,Y,u, warp_scale="auto")
mlab.outline()
mlab.axes()
