"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
-------------------------------------------------------------------------------
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : Poisson_spectral
Created : Mon May 13 16:41:01 2019
"""

import numpy as np


N = 51
T = 100

#Spatial Variables
La = 0
Lb = 1
axes = np.linspace(La,Lb,N)
x , y = np.meshgrid(axes,axes)

#k-Space Variables
k_plus = np.arange(0,N/2,1)
k_minus = np.arange(-N/2,0,1)
k = np.hstack((k_plus,k_minus))
kx , ky = np.meshgrid(k,k)