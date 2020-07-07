"""
D E P A R T E M E N   F I S I K A  -  U G M
Reizkian Yesaya_15/383192/PA/16852
email:reizkianyesaya@gmail.com
------------------------------------------------------------

Program : Heat.eq Finite Difference
Created : 15 November 2018
"""

import numpy as np
import matplotlib.pylab as plab
import mayavi.mlab as mlab

Nmax = 100
Niter = 1000
h=0.0001
mu=1
V = np.zeros((Nmax,Nmax),float)

V[50,0]=100 
	
for iter in range(Niter):
	print(iter*100/Niter,"%")
	for i in range(1,Nmax-1):
		for j in range(1,Nmax-1):
			V[i,j]=(-(h/(2*mu))*(V[i+1,j]-V[i-1,j])+(V[i,j+1]+V[i,j-1]))/2

x = range (0,Nmax,1)
y = range (0,Nmax,1)

X,Y = plab.meshgrid(x,y)

def functz(V):
	z = V[X,Y]
	return z

Z = functz(V)

x,y=np.mgrid[0:100:100j,0:100:100j]

mlab.clf()
mlab.surf(x,y,Z)
mlab.axes()
mlab.outline()