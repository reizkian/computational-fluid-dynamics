"""
D E P A R T E M E N   F I S I K A
Reizkian Yesaya_15/383192/PA/16852
program: Driven Oscilator_HALIM
created: 7 September 2018
"""
import numpy as np
import matplotlib.pyplot as plt

def Fn(phi,omega,t):
    #function parameters
    c=g/l
    Fn=-c*np.sin(2*np.pi*phi)+A*np.sin(omega*t)
    return Fn

#PHYSICAL parameters
l=0.5          #meter (lenght of rope)
g=9.8        #meter/s^2 (gravity constant)
A=1.2        #Newton (driven force amplitude)
omega=np.pi  #rad/sec (driven force frecuency)
gamma=0.2   #Ns/m    (damping oscilation)

#Initial Value
t_0=0
phi_0=0

#Numerical parameters
h=0.01      #Performance
Phi=[]      #Array for phi data containment
Time=[]     #Arrat for time data containment
e=np.exp(-gamma*h)

while t_0<=200:
    #ETD iteration for finding next value of phi
    phi_n1=phi_0*e+Fn(phi_0,omega,t_0)*((1/e)-1)/gamma
    
    #preparing variable for iteration
    phi_0=phi_n1
    t_0=t_0+h
    
    #Put the iteration result into arrays
    Phi.append(phi_0)
    Time.append(t_0)
    
plt.title("Driven Oscilation")
plt.grid(True)
plt.plot(Time,Phi,'r')
plt.show()

