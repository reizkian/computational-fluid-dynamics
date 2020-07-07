import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Mydataset = pd.read_csv('path4.csv')
elevation = Mydataset.iloc[:,:].values

z = Mydataset.iloc[:,3].values
x = np.linspace(0,54,1025)
x_resize = np.linspace(0,54,256)
N_elevation= len(z)
Z_512 = np.zeros([256])

def AverageStep(InputData,OutputData):
    InputData_calc = InputData.copy()
    OutputData_calc = OutputData.copy()
    
    na = len(InputData_calc)
    nb = len(OutputData_calc)
    step = int(na/nb)

    for i in range(0,na-step,step):
        contain=0
        for j in range(step):
            contain = contain + InputData_calc[i+j]
        average = contain/step
        pointer = int(i/step+1)
        OutputData_calc[pointer-1]=average
    
    return OutputData_calc
 
Z_resize = AverageStep(z,Z_512)
  
plt.plot(x_resize,Z_resize)
#plt.plot(x,z)
plt.grid(True)
plt.plot      