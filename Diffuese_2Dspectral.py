"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
-------------------------------------------------------------------------------
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : Diffuse_2DSpectral
Created : Fri Apr 26 12:30:10 2019
"""
import numpy as np
import mayavi.mlab as mlab

N = 100
nu = 0.0001
axes = np.linspace(-1,1,N)
X , Y = np.meshgrid(axes,axes)

x = X.T
y = Y.T
r = np.sqrt(x**2 + y**2)
z = u0=1/(np.cosh(10.0*r)**2)

k_plus = np.arange(0,N/2,1)
k_minus = np.arange(-N/2,0,1)
k = np.hstack((k_plus,k_minus))
Kx , Ky = np.meshgrid(k,k)
kx = Kx.T
ky = Ky.T

z_fft = np.fft.fft2(z)
U_kxky= z_fft.copy()

def diffuse2D(tmax):
    Nt = 100 
    dt = tmax/Nt
    for n in range (Nt):
        percentage = n*100/Nt
        print("RUNNIG =",percentage, "%")
        for i in range (0,N):
            for j in range (0,N):
                c = -(kx[i,j]**2+ky[i,j]**2) * nu 
                U_kxky[i,j] = U_kxky[i,j] * np.exp(c* n * dt)
    
    # FINAL NUMERICAL RESULT 
    U_xyt = np.real(np.fft.ifft2(U_kxky))
    
    # Plot Construction 
    mlab.clf()
    mlab.surf(x,y,U_xyt)
    mlab.outline()
    mlab.axes()

print("=== PROGRAM HAS BEEN SUCCESSFUlLY EXECUTED===")
