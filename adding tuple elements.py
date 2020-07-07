"""
D E P A R T E M E N   F I S I K A
Reizkian Yesaya_15/383192/PA/16852
program: adding tuple elements
created: 31 Juli 2018
"""

import matplotlib.pyplot as plt

h=-10
x=[]
y=[]

while h<=10:
    print(h)
    x.append(h)
    y.append(2*h)
    h=h+1


plt.plot(x,y)
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.title('P L O T I N G')
plt.grid(True)
plt.show()
