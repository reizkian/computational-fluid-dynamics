"""
D E P A R T E M E N   F I S I K A - U G M
Bulaksumur Yogyakarta, Kabupaten Sleman 55281
-------------------------------------------------------------------------------
Author  : Reizkian Yesaya .R
Email   : reizkianyesaya@gmail.com
Program : FD_PressureInducedFLow_DataExtraction
Created : Fri May 17 16:46:32 2019
"""

import numpy as np
import matplotlib.pyplot as plt

#Parameter Numerik:
N=100            # grid points
L=1             # ukuran sistem
dx = L/(N-1)
dy = L/(N-1)
dt = 0.00001      # Sensitif terhadap nilai dt, apabila diubah terlalu besar mungkin NAN

#Parameter Fisis:
#(!! dicoba dahulu untuk N_time=50, untuk memastikan program!!)
N_time = 1000      # untuk menghitung 1 detik 
                 # N_time*dt = (1000)*(0.001) = 1 detik   
N_ptime = 10     # step-time untuk tekanan
vis = 0.1    # viskositas kinematik
rho = 1          # massa jenis
nu = vis/rho

#Profile data time
profile1 = N_time/3
profile2 = N_time/2
profile3 = N_time

#Deklarasi Variabel Ruang:
axes1 = np.linspace(0,L,N)
axes2 = np.linspace(0,L,N)
x,y = np.meshgrid(axes1,axes2) 

u = np.zeros([N,N])     #kecepatan arah-x
v = np.zeros([N,N])     #kecepatan arah-y
P = np.zeros([N,N])     #Tekanan
b = np.zeros([N,N])     #source Tekanan

P[0,:] = 1     #Induksi Tekanan pada sebelah kiri

#------------------------------------------------------------------------------
# Mulai Iterasi
#------------------------------------------------------------------------------
for n in range(N_time+1):
    percentage = n*100/N_time
    print("RUNNIG =",percentage, "%")
        
    for i in range (1,N-1):
        for j in range (1,N-1):
            u_xcd = ( u[i+1,j] - u[i-1,j] ) / 2 / dx  # du/dx central difference 
            u_ycd = ( u[i,j+1] - u[i,j-1] ) / 2 / dx  # du/dy central difference
            v_xcd = ( v[i+1,j] - v[i-1,j] ) / 2 / dx  # dv/dx central difference
            v_ycd = ( v[i,j+1] - v[i,j-1] ) / 2 / dx  # dv/dy central difference
            b[i,j] = rho*(u_xcd+v_ycd)/dt - rho*(u_xcd**2+v_ycd**2+2*u_ycd*v_xcd)
    
    for t in range(N_ptime):
        for i in range (1,N-1):
            for j in range (1,N-1):
                P_xx = (P[i+1,j] + P[i-1,j]) * (dy**2) # turunan P dua kali x
                P_yy = (P[i,j+1] + P[i,j-1]) * (dx**2) # turunan P dua kali y
                #Nilai tekanan yang dicari         
                P[i,j] = (P_xx + P_yy - b[i,j]*(dx**2)*(dy**2)) / (dx**2+dy**2) /2 
        
        #Syarat Batas Tekanan
        P[:,0]  = P[:,1]    # dP/dy = 0  pada y = 0
        P[:,-1] = P[:,-2]   # dP/dy = 0  pada y = 1
        
    un = u.copy()
    vn = v.copy()   
    for i in range(1,N-1):
        for j in range(1,N-1):
            u_x = (un[i,j] - un[i-1,j]) / dx # u turunan x
            u_y = (un[i,j] - un[i,j-1]) / dy # u turunan y   
            v_x = (vn[i,j] - vn[i-1,j]) / dx # v turunan x
            v_y = (vn[i,j] - vn[i,j-1]) / dy # v turunan y           
            
            P_x = (P[i+1,j] - P[i-1,j]) / 2 / dx # P turunan x
            P_y = (P[i,j+1] - P[i,j-1]) / 2 / dy # P turunan y
            
            u_xx = (un[i+1,j] - 2*u[i,j] + un[i-1,j]) / (dx**2) # u turunan x, dua kali
            u_yy = (un[i,j+1] - 2*u[i,j] + un[i,j-1]) / (dx**2) # u turunan y, dua kali
            v_xx = (vn[i+1,j] - 2*v[i,j] + vn[i-1,j]) / (dy**2) # v turunan x, dua kali
            v_yy = (vn[i,j+1] - 2*v[i,j] + vn[i,j-1]) / (dy**2) # v turunan y, dua kali
            
            #Nilai kecepatan yang dicari 
            u[i,j] = un[i,j] + dt*(-u[i,j]*u_x - v[i,j]*u_y - (P_x/rho) + vis*(u_xx+u_yy))
            v[i,j] = vn[i,j] + dt*(-u[i,j]*v_x - v[i,j]*v_y - (P_y/rho) + vis*(v_xx+v_yy))
        
    #Syarat batas kecepatan
    u[:,-1] = 0  #u(x,y=1) = 0
    u[:,0]  = 0  #u(x,y=0) = 0
    u[0,:]  = 0  #u(x=0,y) = 0
    u[-1,:] = 0  #u(x=1,y) = 0
        
    v[:,-1] = 0  #u(x,y=1) = 0
    v[:,0]  = 0  #u(x,y=0) = 0
    v[0,:]  = 0  #u(x=0,y) = 0
    v[-1,:] = 0  #u(x=1,y) = 0
    
    
    # D A T A   E X T R A C T I O N   C O N D I O T I O N
    #---------------------------
    # ketika iterasi berlangsung, data disimpan pada variabel2 dibawah ini 
    # kondisi extract diungkapkan dalam syarat "if" 
    # variabel di TRANSPOSE agar susunan data sesuai dengan spesifikasi matplotlib
    # transpose hanya untuk kepentingan plotting, bukan untuk manipulasi matematis
    #---------------------------
    if n == int(profile1): #profile 1 (menampung data ketika t=0.1)
        u1 = u.copy()
        v1 = v.copy()
        P1 = P.copy()
        P_sx1 = P1[0:N-1,int(N/2)]     # tekanan P(x) (y=L/2 t=0.1)
        u1_central = u1[int(N/2),0:N]  # kecepatan u sumbu simetri-y
        v1_central = v1[0:N,int(N/2)]  # kecepatan x sumbu simetri-x
        u1 = u1.T
        v1 = v1.T
        P1 = P1.T
        VelocityMagnitude1 = np.sqrt(u1**2+v1**2)
        print("---------------> Profile 1 saved")
    if n == int(profile2): #profile 2 (menampung data ketika t=0.5)
        u2 = u.copy()
        v2 = v.copy()
        P2 = P.copy()
        P_sx2 = P2[0:N-1,int(N/2)]    # tekanan P(x) (y=L/2 t=0.5)
        u2_central = u2[int(N/2),0:N] # kecepatan u sumbu simetri-y
        v2_central = v2[0:N,int(N/2)] # kecepatan v sumbu simetri-x
        u2 = u2.T
        v2 = v2.T
        P2 = P2.T
        VelocityMagnitude2 = np.sqrt(u2**2+v2**2)
        print("---------------> Profile 2 saved")
    if n == int(profile3): #profile 3 (menampung data ketika t=1)
        u3 = u.copy()
        v3 = v.copy()
        P3 = P.copy()
        P_sx3 = P3[0:N-1,int(N/2)]     # tekanan P(x) (y=L/2 t=1)
        u3_central = u3[int(N/2),0:N]  # kecepatan u sumbu simetri-y
        v3_central = v3[0:N,int(N/2)]  # kecepatan v sumbu simetri-x
        u3 = u3.T
        v3 = v3.T
        P3 = P3.T
        VelocityMagnitude3 = np.sqrt(u3**2+v3**2)
        print("---------------> Profile 3 saved")
#------------------------------------------------------------------------------
#Selesai Iterasi
#------------------------------------------------------------------------------


print("V I C O U S I T Y    C H A N G E D ")


visa = 0.1    # viskositas kinematik
rho = 1          # massa jenis
nu = vis/rho

#Profile data time
profile1 = N_time/3
profile2 = N_time*2/3
profile3 = N_time

#Deklarasi Variabel Ruang:
axes1 = np.linspace(0,L,N)
axes2 = np.linspace(0,L,N)
x,y = np.meshgrid(axes1,axes2) 

ua = np.zeros([N,N])     #kecepatan arah-x
va = np.zeros([N,N])     #kecepatan arah-y
Pa = np.zeros([N,N])     #Tekanan
ba = np.zeros([N,N])     #source Tekanan

Pa[0,:] = 1     #Induksi Tekanan pada sebelah kiri

#------------------------------------------------------------------------------
# Mulai Iterasi
#------------------------------------------------------------------------------
for n in range(N_time+1):
    percentage = n*100/N_time
    print("RUNNIG =",percentage, "%")
        
    for i in range (1,N-1):
        for j in range (1,N-1):
            ua_xcd = ( ua[i+1,j] - ua[i-1,j] ) / 2 / dx  # du/dx central difference 
            ua_ycd = ( ua[i,j+1] - ua[i,j-1] ) / 2 / dx  # du/dy central difference
            va_xcd = ( va[i+1,j] - va[i-1,j] ) / 2 / dx  # dv/dx central difference
            va_ycd = ( va[i,j+1] - va[i,j-1] ) / 2 / dx  # dv/dy central difference
            ba[i,j] = rho*(ua_xcd+va_ycd)/dt - rho*(ua_xcd**2+va_ycd**2+2*ua_ycd*va_xcd)
    
    for t in range(N_ptime):
        for i in range (1,N-1):
            for j in range (1,N-1):
                Pa_xx = (Pa[i+1,j] + Pa[i-1,j]) * (dy**2) # turunan P dua kali x
                Pa_yy = (Pa[i,j+1] + Pa[i,j-1]) * (dx**2) # turunan P dua kali y
                #Nilai tekanan yang dicari         
                Pa[i,j] = (Pa_xx + Pa_yy - ba[i,j]*(dx**2)*(dy**2)) / (dx**2+dy**2) /2 
        
        #Syarat Batas Tekanan
        Pa[:,0]  = Pa[:,1]    # dP/dy = 0  pada y = 0
        Pa[:,-1] = Pa[:,-2]   # dP/dy = 0  pada y = 1
        
    uan = u.copy()
    van = v.copy()   
    for i in range(1,N-1):
        for j in range(1,N-1):
            ua_x = (uan[i,j] - uan[i-1,j]) / dx # u turunan x
            ua_y = (uan[i,j] - uan[i,j-1]) / dy # u turunan y   
            va_x = (van[i,j] - van[i-1,j]) / dx # v turunan x
            va_y = (van[i,j] - van[i,j-1]) / dy # v turunan y           
            
            Pa_x = (Pa[i+1,j] - Pa[i-1,j]) / 2 / dx # P turunan x
            Pa_y = (Pa[i,j+1] - Pa[i,j-1]) / 2 / dy # P turunan y
            
            ua_xx = (uan[i+1,j] - 2*ua[i,j] + uan[i-1,j]) / (dx**2) # u turunan x, dua kali
            ua_yy = (uan[i,j+1] - 2*ua[i,j] + uan[i,j-1]) / (dx**2) # u turunan y, dua kali
            va_xx = (van[i+1,j] - 2*va[i,j] + van[i-1,j]) / (dy**2) # v turunan x, dua kali
            va_yy = (van[i,j+1] - 2*va[i,j] + van[i,j-1]) / (dy**2) # v turunan y, dua kali
            
            #Nilai kecepatan yang dicari 
            ua[i,j] = uan[i,j] + dt*(-ua[i,j]*ua_x - va[i,j]*ua_y - (Pa_x/rho) + visa*(ua_xx+ua_yy))
            va[i,j] = van[i,j] + dt*(-ua[i,j]*va_x - va[i,j]*va_y - (Pa_y/rho) + visa*(va_xx+va_yy))
        
    #Syarat batas kecepatan
    ua[:,-1] = 0  #u(x,y=1) = 0
    ua[:,0]  = 0  #u(x,y=0) = 0
    ua[0,:]  = 0  #u(x=0,y) = 0
    ua[-1,:] = 0  #u(x=1,y) = 0
        
    va[:,-1] = 0  #u(x,y=1) = 0
    va[:,0]  = 0  #u(x,y=0) = 0
    va[0,:]  = 0  #u(x=0,y) = 0
    va[-1,:] = 0  #u(x=1,y) = 0
    
    
    # D A T A   E X T R A C T I O N   C O N D I O T I O N
    #---------------------------
    # ketika iterasi berlangsung, data disimpan pada variabel2 dibawah ini 
    # kondisi extract diungkapkan dalam syarat "if" 
    # variabel di TRANSPOSE agar susunan data sesuai dengan spesifikasi matplotlib
    # transpose hanya untuk kepentingan plotting, bukan untuk manipulasi matematis
    #---------------------------
    if n == int(profile1): #profile 1 (menampung data ketika t=0.1)
        ua1 = ua.copy()
        va1 = va.copy()
        Pa1 = Pa.copy()
        Pa_sx1 = Pa1[0:N-1,int(N/2)]     # tekanan P(x) (y=L/2 t=0.1)
        ua1_central = ua1[int(N/2),0:N]  # kecepatan u sumbu simetri-y
        va1_central = va1[0:N,int(N/2)]  # kecepatan x sumbu simetri-x
        ua1 = ua1.T
        va1 = va1.T
        Pa1 = Pa1.T
        VelocityMagnitudea1 = np.sqrt(ua1**2+va1**2)
        print("---------------> Profile 1 saved")
    if n == int(profile2): #profile 2 (menampung data ketika t=0.5)
        ua2 = ua.copy()
        va2 = va.copy()
        Pa2 = Pa.copy()
        Pa_sx2 = Pa2[0:N-1,int(N/2)]    # tekanan P(x) (y=L/2 t=0.5)
        ua2_central = ua2[int(N/2),0:N] # kecepatan u sumbu simetri-y
        va2_central = va2[0:N,int(N/2)] # kecepatan v sumbu simetri-x
        ua2 = ua2.T
        va2 = va2.T
        Pa2 = Pa2.T
        VelocityMagnitudea2 = np.sqrt(ua2**2+va2**2)
        print("---------------> Profile 2 saved")
    if n == int(profile3): #profile 3 (menampung data ketika t=1)
        ua3 = ua.copy()
        va3 = va.copy()
        Pa3 = Pa.copy()
        Pa_sx3 = Pa3[0:N-1,int(N/2)]     # tekanan P(x) (y=L/2 t=1)
        ua3_central = ua3[int(N/2),0:N]  # kecepatan u sumbu simetri-y
        va3_central = va3[0:N,int(N/2)]  # kecepatan v sumbu simetri-x
        ua3 = u3.T
        va3 = v3.T
        Pa3 = P3.T
        VelocityMagnitudea3 = np.sqrt(ua3**2+va3**2)
        print("---------------> Profile 3 saved")
#------------------------------------------------------------------------------
#Selesai Iterasi
#------------------------------------------------------------------------------

#CODE UNTUK PLOT 
total_time = N_time*dt
colorMagnitude = "jet"
colorPressure = "coolwarm"

y_plot = np.linspace(0,L,N)
x_plot = np.linspace(0,L,N)

yp_plot = np.linspace(0,L,N-1)
xp_plot = np.linspace(0,L,N-1)


fig1 =  plt.figure() #left profile
plt.plot(yp_plot,P_sx3,'r*-', label='vis = 0.1')
plt.plot(yp_plot,Pa_sx3,'bx-', label='vis = 0.001')
plt.grid()
plt.xlabel('y')
plt.ylabel('P(x)')
plt.title('Tekanan P(x) pada y=L/2')
plt.grid(True)
plt.legend()
plt.show()

fig7 =  plt.figure() # u profile
plt.plot(y_plot,u3_central,'r*-', label='vis = 0.1')
plt.plot(y_plot,ua3_central,'bx-', label='vis = 0.01')
plt.grid()
plt.xlabel('y')
plt.ylabel('u(y)')
plt.title('Profil u(y) pada x=0.5')
plt.grid(True)
plt.legend()
plt.show()

fig8 =  plt.figure() # v profile
plt.plot(x_plot,v3_central,'r*-', label='vis = 0.1')
plt.plot(x_plot,va3_central,'bx-', label='vis = 0.1')
plt.grid()
plt.xlabel('x')
plt.ylabel('v(x)')
plt.title('Profil v(x) pada y=0.5')
plt.grid(True)
plt.legend()
plt.show()