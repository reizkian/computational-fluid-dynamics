"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
-------------------------------------------------------------------------------
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : FiniteElement
Created : Mon May 27 11:17:13 2019
"""

import numpy as np
import mayavi.mlab as mlab

axes = np.linspace(0,1,100)
x , y = np.meshgrid(axes,axes)

u = -x*(x-3)/2

mlab.clf()
mlab.surf(x.T,y.T,u,warp_scale="auto")
mlab.outline()
mlab.axes()
