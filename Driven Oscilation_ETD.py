"""
D E P A R T E M E N   F I S I K A  -  U G M
Reizkian Yesaya_15/383192/PA/16852
email:reizkianyesaya@gmail.com
------------------------------------------------------------

Program : Driven Oscilation ETD 
Created : 6 October 2018
"""
import numpy as np
import matplotlib.pyplot as plt

#Numerical Constant
t0=0
tmax=1300
h=0.01

#Physical Constant
A=1.12           #Amplitude of driven force
alfa=0.2        #Damping coeficient
omega=np.pi/10  #Frecuency of driven force
g=9.8           #Gravity acceleration
l=1             #Lenght of the rope

#Initial condition
phi0 = 0.0
v0   = 0.0

#Array for storing numerical itteration
PHI  = []
V 	 = []
TIME = []

def phi(phi0,v0):
    phi=phi0+h*v0
    return phi

def integral(t0,t1,phi0):
    sigma=0
	
    def Q(phi0,t0):
        Q=np.exp(alfa*t0)*((-g/l)*np.sin(np.pi*phi(phi0,v0))+A*np.sin(omega*t0))
        return Q
	
    n=(t1-t0)/100
    while t0<=t1:
        q=Q(phi0,t0)
        sigma=sigma+q
        t0=t0+n
    return sigma*n
  
def vn(phi0,v0,t0):
    t0=t0
    t1=t0+h
    vn_1=v0*np.exp(-alfa*h)+integral(t0,t1,phi0)/(np.exp(alfa*(t0+h)))
    return vn_1


print("------------------------------------------")
print("TIME","          ","PHI","            ","V")
print("------------------------------------------")

while t0<=tmax:
	TIME.append(t0)
	V.append(v0)
	PHI.append(phi0)

	print(t0,"    ",phi0,"       ",v0)
	
	t0 	 = t0+h
	phi0 = phi(phi0,v0)
	v0 	 = vn(phi0,v0,t0)
	
	
	
plt.title("Driven Oscilation")
plt.grid(True)
plt.plot(TIME,PHI,'r')
#plt.plot(TIME,V,'b')
plt.show()	