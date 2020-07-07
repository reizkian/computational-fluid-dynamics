import numpy as np
import matplotlib.pyplot as plt
import math

Lx=1
Ly=1
ratio = Ly/Lx
Nx=100
Ny=int(ratio*Nx)
dx = Lx/(Nx-1)
dy = Ly/(Ny-1)
dt = 0.00001

#Parameter Fisis:
#(!! dicoba dahulu untuk N_time=50, untuk memastikan program!!)
N_time = 500    # untuk menghitung 1 detik 
                # N_time*dt = (1000)*(0.001) = 1 detik   
N_ptime = 10    # step-time untuk tekanan
vis = 0.1       # viskositas kinematik
rho = 1         # massa jenis
nu = vis/rho
Gx = 0
Gy = 0

#Profile data time
profile1 = N_time/3
profile2 = N_time*2/3
profile3 = N_time

u = np.zeros([Nx,Ny])     #kecepatan arah-x
v = np.zeros([Nx,Ny])     #kecepatan arah-y
P = np.zeros([Nx,Ny])     #Tekanan
b = np.zeros([Nx,Ny])     #source Tekanan

P[0,:] = 10     #Induksi Tekanan pada sebelah kiri

#O B J E C T (definition)
object_array = np.zeros([Nx,Ny])

r = 0.2
pos_x = 0.5
pos_y = 0.5

Nr = round((Nx*r/Lx)/2+(Ny*r/Ly)/2)
Na = round(Nx*pos_x/Lx)
Nb = round(Ny*pos_y/Ly)
for i in range(Nx):
    for j in range(Ny):
        argument = np.sqrt( (i-Na)**2 + (j-Nb)**2 )
        if argument > Nr:
            object_array[i,j] = 0
        if argument <= Nr:
            object_array[i,j] = 1
            
Nd = Nr*2

nx = np.arange(Na-Nr,Na+Nr,1)
ny = np.floor(np.sqrt((Nr)**2-(nx-Na)**2 ))
nx = nx.astype(int)
ny = ny.astype(int)
P_tetha = np.zeros([Nd])

for i in range (Nd):
    Ni = nx[i]
    Nj = ny[i]
    P_tetha[i] = object_array[Ni,Nj]
 
plt.plot(nx,ny)
plt.show()