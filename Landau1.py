"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
-------------------------------------------------------------------------------
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : Landau_NavierStokes
Created : Tue Apr 30 11:16:56 2019
"""

import numpy
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pylab as p
import matplotlib.pyplot as plt
import mayavi.mlab as mlab

print ("PROGRAM IS RUNNING, please wait!")
niter = 100
Nxmax = 70
Nymax = 20
IL = 10
H = 8 
T = 8
h = 1

u = numpy.zeros([Nxmax+1,Nymax+1],float)
w = numpy.zeros([Nxmax+1,Nymax+1],float)

V0 = 1
omega = 0.1
nu = 1
iter = 0
R = V0 * h / nu


def borders():
	for i in range(0,Nxmax+1):
		for j in range(0,Nymax+1):
			w[i,j] = 0
			u[i,j] = j * V0
	
	for i in range(0,Nxmax+1):
		u[i,Nymax] = u[i,Nymax-1] + V0 * h
		w[i,Nymax-1] = 0
		
	for j in range(0,Nymax+1):
		u[i,j] = u[0,j]
		w[0,j] = 0
		
	for i in range(0,Nxmax+1):
		if i <= IL and i >= IL + T:
			u[i,0] = 0
			w[i,0] = 0
			
	for j in range(0,Nymax+1):
		w[Nxmax,j] = w[Nxmax-1,j]
		u[Nxmax,j] = u[Nxmax-1,j]
		


def beam():
	for j in range (0,H+1):
		w[IL,j] = -2 * u[IL-1,j] / (h*h)
		w[IL+T,j] = -2 * u[IL+T+1,j] / (h*h)
	
	for i in range(IL , IL+T+1):
		w[i,H-1] = -2 * u[i,H] / (h*h)
	
	for i in range(IL , IL+T+1):
		for j in range(0,H+1):
			u[IL,j] = 0
			u[IL+T,j] = 0
			u[i,H] = 0
			 

def relax():
	beam()
	for i in range(1,Nxmax):
		for j in range(1,Nymax):
			r1 = omega * ((u[i+1,j] + u[i-1,j] + u[i,j+1] + u[i,j-1] + h*h*w[i,j]) / 4-u[i,j] )
			u[i,j] += r1
		
	for i in range(1,Nymax):
		for j in range (1,Nymax):
			a1 = w[i+1,j] + w[i-1,j] + w[i,j+1] + w[i,j-1]
			a2 = (u[i,j+1] - u[i,j-1]) * (w[i+1,j] - w[i-1,j])
			a3 = (u[i+1,j] - u[i-1,j]) * (w[i,j+1] - w[i,j-1])
			r2 = omega * ((a1-(R/4.) * (a2 - a3))/4. - w[i,j])
			w[i,j] += r2

borders()
while(iter <= niter):
    iter += 1
    percentage = iter*100/niter
    print("RUNNIG =",percentage, "%")
    relax()

for i in range(0,Nxmax+1):
	for j in range(0,Nymax+1):
		u[i,j] = u[i,j] / V0 / h

x = numpy.arange(0 , Nxmax-1)
y = numpy.arange(0 , Nymax-1)
		
X , Y = p.meshgrid(x,y)

def functz(u):
	z = u[X,Y]
	return z

Z = functz(u)

fig = p.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X,Y,Z, color = 'r')
ax.set_xlabel('X')
ax.set_xlabel('Y')
ax.set_zlabel('Stream Plot')
p.show()	 

X=X.T
Y=Y.T
mlab.clf()
mlab.surf(X,Y,Z, representation="wireframe")
mlab.outline()
mlab.axes()








