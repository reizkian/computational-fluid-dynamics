"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
===============================================================================
Author  : Fahrudin Nugroho
Program : Combustion ETD_RK_Euler
Created : Mon Mar 18 16:22:23 2019
==============================================================================
"""

def fun(y):
    import numpy as np
    return 10*(y*y)-20*(y*y*y)

import matplotlib.pyplot as plt
import numpy as np
datax=[]
datay=[]
y0 = 0.01
t0 = 0
h = 0.4

for i in range(200):
    t1 = t0+h
    k1 = h*fun(y0)
    k2 = h*fun(y0 + k1/2)
    k3 = h*fun(y0 + k2/2)
    k4 = h*fun(y0 + k3)
    y1 = y0 + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    y0 = y1
    t0 = t1
    datax.append(t0)
    datay.append(y0)

def gun(y):
    import numpy as np
    return 10*(y*y)-20*(y*y*y)-0.1*y
c = 0.1
y0 = 0.01
t0 = 0
h = 0.4
datax1=[]
datay1=[]
for i in range (200):
    t1 = t0 + h
    y1 =y0*np.exp(c*h) + gun(y0)*(np.exp(c*h)-1)/(c)
    datay1.append(y0)
    datax1.append(t0)
    t0 = t1
    y0 = y1

y0 = 0.01
t0 = 0
h = 0.4
datax2=[]
datay2=[]
for i in range (200):
    t1 = t0 + h
    y1 = y0 + h*fun(y0)
    t0 = t1
    y0 = y1
    datax2.append(t0)
    datay2.append(y0)

#print (datax[1], datax[2])
#u = [l[1] for l in datax]
#print (u)
fig1 =  plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(datax,datay, '-o')
plt.title('runge kuta')
plt.grid(True)
plt.axis([0,5000, 0.0, 1.5])

fig2 =  plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(datax1,datay1, '-o')
plt.title('ETD')
plt.grid(True)
plt.axis([0,5000, 0.0, 1.5])

fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
ax3.plot(datax2,datay2, '-o')
plt.title('Euler')
plt.grid(True)
plt.axis([0,5000, 0.0, 1.5])

fig4 = plt.figure()
ax4 = fig4.add_subplot(111)
ax4.plot(datax,datay,'-o', label = 'runge kuta')
ax4.plot(datax,datay1,'-o', label = 'etd')
ax4.plot(datax,datay2,'-o', label = 'euler')
plt.legend()
plt.title('RK , ETD, Euler')
plt.grid(True)
plt.axis([0,100, 0.0, 1.0])

plt.show()