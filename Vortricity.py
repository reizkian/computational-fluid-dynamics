"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
-------------------------------------------------------------------------------
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : Vortricity
Created : Tue Apr 23 13:03:48 2019
"""
import numpy as np
import matplotlib.pyplot as plt

Ngrid = 128
vsc = 0.005
h = 2 * np.pi / Ngrid

axis = h * np.arange( 0, Ngrid, 1 )
x , y = np.meshgrid(axis,axis)

# Initial value votricity
w1 = np.exp(-((x-np.pi+np.pi/5)**2 + (y-np.pi+np.pi/5)**2)/0.3)
w2 = np.exp(-((x-np.pi-np.pi/5)**2 + (y-np.pi+np.pi/5)**2)/0.2)
w3 = np.exp(-((x-np.pi-np.pi/5)**2 + (y-np.pi-np.pi/5)**2)/0.4)
omega = w1 - w2 + w3

# Generate the plot
fig, ax = plt.subplots()
cmap = ax.pcolormesh(x, y, omega)
fig.colorbar(cmap)
plt.show(fig)
