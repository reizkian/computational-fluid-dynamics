"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
===============================================================================
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : NS1D
Created : Thu Mar 21 15:42:59 2019
==============================================================================
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 1), ylim=(-1, 2))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(T):
    #Numerical properties
    L=1
    N=1000
    x=np.linspace(0,L,N+1)
    
    dk=np.pi/L
    k_plus=np.arange(1,N/2+2,1)
    k_minus=np.arange(-N/2+1,0,1)
    k_array=np.hstack((k_plus,k_minus))
    k=k_array*dk
    k2=k**2
    img=(0+1.j)
    
    #Physical Value
    nu=0.01
    rho=1
    Press=-x*10
    
    def df_dx(y):
        dfdx=np.zeros(N+1)
        for i in range(0,N+1):
            if i <= N-1:
                dfdx[i] = (Press[i+1]-Press[i])/(L/N)
            if i == N:
                dfdx[i]=dfdx[i-1]
        return dfdx
    
    u0=1/(np.cosh(100.0*x)**2)
    u0_hat=np.fft.fft(u0)
    A=u0_hat.copy()
    
    
    #ETD handling
    U2=u0**2
    U2_fft=np.fft.fft(U2)
    dP_dx=df_dx(Press)
    
    tmax=1
    N_t=1000
    dt=tmax/N_t
    
    #MONITOR
    Fn_monitor=np.zeros(N,dtype=complex)
    ech_monitor=np.zeros(N,dtype=complex)
    
    for i in range (0,N):
            ech=np.exp(-k2[i]*nu*(T*dt))
            Fn=-(1/rho)*dP_dx[i]-(img*k[i]*U2_fft[i]/2)
            ech_monitor[i]=ech
            Fn_monitor[i]=Fn
            A[i]=A[i]*ech+Fn*(ech-1)/(-k2[i]*nu)
            
    uT=np.real(np.fft.ifft(A))        
     

    line.set_data(x, uT)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1000, interval=10, blit=True)

plt.grid()
plt.xlabel('position(x)')
plt.ylabel('u(x,t)')
plt.title('VELOCITY PROFILE')
plt.show()
anim.save('NS1D.mp4', fps=30, extra_args=['-vcodec', 'libx264'])