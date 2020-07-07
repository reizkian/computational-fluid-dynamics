"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
-------------------------------------------------------------------------------
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : 
Created : Wed Apr 10 09:48:16 2019
"""

import numpy as np
import mayavi.mlab as mlab

x , y = np.mgrid[ -10:10:101j , -10:10:101j ]
r = np.sqrt( x**2 + y**2 )
z = np.sin(r)/r

mlab.outline(line_width=2.5)
mlab.surf(x,y,z) 