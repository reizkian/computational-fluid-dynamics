"""
D E P A R T E M E N   F I S I K A  -  U G M
Reizkian Yesaya_15/383192/PA/16852
email:reizkianyesaya@gmail.com
------------------------------------------------------------

Program : PDE Electrostatics_Laplace Potential_rho
Created : 2 November 2018
"""

import numpy as np
import matplotlib.pylab as plab
import mayavi.mlab as mlab

Nmax = 100
Niter = 100
V = np.zeros((Nmax,Nmax),float)

#for k in range(1,Nmax-1):
#	V[k,0]=0

for k in range(1,Nmax-1):
	V[k,50]=1000
	
for iter in range(Niter):
	for i in range(1,Nmax-1):
		for j in range(1,Nmax-1):
			V[i,j]=0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])

x = range (0,Nmax,1)
y = range (0,Nmax,1)

X,Y = plab.meshgrid(x,y)

def functz(V):
	z = V[X,Y]
	return z

Z = functz(V)

x,y=np.mgrid[0:100:100j,0:100:100j]

mlab.clf()
#mlab.surf(x,y,Z, representation="wireframe")
mlab.surf(x,y,Z)
#mlab.title("Laplace Potential")
mlab.axes()
mlab.outline()