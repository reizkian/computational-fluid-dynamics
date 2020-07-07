"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
===============================================================================
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : Difuse Realtime
Created : Thu Mar 21 15:42:59 2019
==============================================================================
"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-1, 1), ylim=(0, 1))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(T):
    l=2
    N=512
    dx=l/N
    x_array=np.arange(1-N/2,N/2+1,1)
    x=x_array*dx
    
    nu=0.0005

    dk=np.pi/l
    k_plus=np.arange(0,N/2+1,1)
    k_minus=np.arange(-N/2+1,0,1)
    k_array=np.hstack((k_plus,k_minus))
    k=k_array*dk
    k2=k**2
    
    u0=1/(np.cosh(10.0*x)**2)
    u0_hat=np.fft.fft(u0)
    uT=np.real(np.fft.ifft(np.exp(-nu*k2*T)*u0_hat))
    line.set_data(x, uT)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1000, interval=20, blit=True)

plt.grid()
plt.xlabel('position')
plt.ylabel('Temperature')
plt.title('TEMPERATURE DIFUSE')
plt.show()