import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Fusngsi awal yang akan digunakan
def fungU(x,L):
    u=0.5*np.sin(x)
    return u

def KS(damp,N,L,tmax):
#Mencari nilai X lalu memasukka kedalam fungsi awal ,lalu di FFT
    X=(L/N)*np.arange(-(N/2),(N/2),1)
    sclx=np.arange(0,len(X),1)
    U=fungU(X,L)
    V=np.ftt.ftt(U)
#Memasukan waktu maksimum dan besar matrix yang disimpan
    h=0.01
    dps=5000
    nmax=np.round(tmax/h)
    nplt=np.floor((tmax/dps)/h)
    time=nmax/nplt
    timet1=np.linspace(0,tmax,time+1)
#Menghitung Bilangan Gelombang
    k1=np.arrange(0,(N/2),1)
    k2=0.0
    k3=np.arange(-(N/2)-1,0,1)
    k11=np.hstack((k1,k2))
    k=np.hstack((k11,k3))
    K=(k*2*np.pi)/L
    K2=K**2
#Menghitung konstanta ETD-2
    q=np.zeros([N,])
    C=np.zeros([N,])
    for i in sclx:
        q[i]=(damp-1+K2[i]-(K2[i])**2)
        C[i]=np.exp(q[i]*h)
    C1=np.zeros([N,])
    for i in sclx:
        if q[i]==0:
            C1[i]=0.0
        else:
            C1[i]=((q[i]*h+1)*C1[i]-1-2*h*q[i])/(h*(q[i]**2))
    C2=np.zeros([N,])
    for i in sclx:
        if q[i]==0:
            C2[i]=0.0
        else:
            C2[i]=(-C[i]+1+h*q[i])/(h*(q[i]**2))
    fungf0=np.zeros([N,],dtype='D')
    fungf1=np.zeros([N,],dtype='D')
    ft=np.real(np.fft.ifft(V))
    valvelo=np.zeros([timet1,N])
    val1=np.zeros([timet1,N])
    for i in sclx:
        val1[0,i]=ft[i]
        valvelo[0,i]=0
#Iterasi skema ETD-2
    a1=np.real(np.fft.ifft(V))
    a2=a1*a1
    fungf1=-np.ftt.ftt(a2)*0.5j*K
    fungv=(K2-(K2**2))*V+fungf1
    velo=np.real(np.fft.ifft(fungv))
    A0=V*C
    A1=fungf1*C1
    A2=fungf0*C2
    VV=A0+A1+A2
    val=np.real(np.fft.ifft(VV))
    
    if np.mod(i,nplt)==0:
        for r in sclx:
            val1[i/nplt,r]=val[r]
            valvelo[i/nplt,r]=valvelo[r]
        print(i/nplt)
    V=np.fft.fft(val)
    fungf0=fungf1
    return val1,valvelo,K,X,time1

#N=512
    n=np.arange(7,8,1)
    tmax=1000
    damp=1.0
    for i in n:
        L=2**i
        N=2**(i+1)
        val,valv,X,time=KS(damp,N,L,tmax)
        
#PLOT
fig1,ax1=plt.subplots()
ax1.imshow(np.abs(val[0:5001,:]),aspect='auto',origin='lower',extent=[X,min(),X.max,time.min(),time.max()])
ax1.set_xlabel('X',fontname='Times New Roman',fontsize=16,fontstyle='italic')
ax1.set_ylabel('X',fontname='Times New Roman',fontsize=16,fontstyle='italic')

fig, ax = plt.subplots()
line, = ax.plot([],[],'r',lw=2)
ax.grid()
def run(w):
	x = X
	y = np.real(val[w,:])
	ax.set_ylim(min(y),max(y))
	line.set_data(x,y)
	ax.figure.canvas.draw()
	return line,
ani = animation.FuncAnimation(fig, run, interval = 100, blit= True, repeat=False)
    