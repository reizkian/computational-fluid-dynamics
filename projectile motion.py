"""
D E P A R T E M E N   F I S I K A
Reizkian Yesaya_15/383192/PA/16852
program: projectile motion
created: 1 August 2018
"""

import numpy as np
import matplotlib.pyplot as plt
import time

s=time.time()
"function declaration"
def x_distance(t,theta):
    vx=velocity*np.cos(theta)
    x_distance=vx*t
    return x_distance

def y_distance(t,theta):
    vy=velocity*np.sin(theta)-g*t
    y_distance=(vy*t)-0.5*g*(t**2)
    return y_distance

def y_max(t,theta):
    mid_air=(t/2)
    vy=velocity*np.sin(theta)-g*mid_air
    y_max=(vy*mid_air)-0.5*g*(mid_air**2)
    return y_max
    
"variable declaration"
#INPUT PARAMETERS
velocity=50       #in meters/second
th1=90
th2=45
th3=30
theta1=(th1/180)*np.pi
theta2=(th2/180)*np.pi
theta3=(th3/180)*np.pi

#CALCULATION PARAMETERS
g=9.8           #gravity acceleration
dt=0.01         #in seconds

#initial condition
t_01=0
t_02=0
t_03=0
y_01=0
x_01=0
y_02=0
x_02=0
y_03=0
x_03=0

#GRAPH PARAMETERS
y1=[]            #alttitude in meters
x1=[]            #distances in meters
y2=[]            #alttitude in meters
x2=[]            #distances in meters
y3=[]            #alttitude in meters
x3=[]            #distances in meters

while y_01>=0:
    x_01=x_distance(t_01,theta1)
    y_01=y_distance(t_01,theta1)
    #print(t_0,"    ",x_0,"    ",y_0)
    
    x1.append(x_distance(t_01,theta1))
    y1.append(y_distance(t_01,theta1))
    #x2.append(x_distance(t_0,theta2))
    #y2.append(y_distance(t_0,theta2))
    #x3.append(x_distance(t_0,theta3))
    #y3.append(y_distance(t_0,theta3))
    t_01=t_01+dt
    
while y_02>=0:
    x_02=x_distance(t_02,theta2)
    y_02=y_distance(t_02,theta2)
    #print(t_0,"    ",x_0,"    ",y_0)
    
    #x1.append(x_distance(t_0,theta1))
    #y1.append(y_distance(t_0,theta1))
    x2.append(x_distance(t_02,theta2))
    y2.append(y_distance(t_02,theta2))
    #x3.append(x_distance(t_0,theta3))
    #y3.append(y_distance(t_0,theta3))
    t_02=t_02+dt
    
while y_03>=0:
    x_03=x_distance(t_03,theta3)
    y_03=y_distance(t_03,theta3)
    #print(t_0,"    ",x_0,"    ",y_0)
    
    #x1.append(x_distance(t_0,theta1))
    #y1.append(y_distance(t_0,theta1))
    #x2.append(x_distance(t_0,theta2))
    #y2.append(y_distance(t_0,theta2))
    x3.append(x_distance(t_03,theta3))
    y3.append(y_distance(t_03,theta3))
    t_03=t_03+dt
    
#------------------------------------------------------
"GRAPHIC PLOT"    
plt.title('Projectile Motion')
plt.xlabel("distances (meters)")
plt.ylabel("altitude (meters)")
plt.grid(True)
plt.plot(x1,y1,'r--')
plt.plot(x2,y2,'g--')            
plt.plot(x3,y3,'b--')
plt.show()
#------------------------------------------------------

print("----------------------------------------------------------------")
print("angle","    ","air_time","         ","X_max","          ","Y_max")
print("----------------------------------------------------------------")
print(th1,"  ",t_01," ",x_01," ",y_max(t_01,theta1))
print(th2,"  ",t_02," ",x_02," ",y_max(t_02,theta2))
print(th3,"  ",t_03," ",x_03," ",y_max(t_03,theta3))
print("----------------------------------------------------------------")

f=time.time()
run=f-s
print(run)