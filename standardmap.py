import numpy as np
import matplotlib.pyplot as plt
import random
nit=1000000
k=0.97
def devV(q):
    return k/(2*np.pi)*np.sin(2*np.pi*q)
def plotinit(q0,p0):
    data=[np.array([q0,p0])]
    
    for i in range(nit-1):
        tmp=q0
        p0=p0+devV(q0)
        q0=q0+p0

        q0=(q0)%1
        p0=(p0+1)%1
        data.append(np.array([q0,p0]))
    np.array(data)
    data=np.transpose(data)
    plt.plot(data[0],data[1],'.',markersize=0.8)

    return
N=8
for j in range(N):
     
     True
       #plotinit(0.6,0.3+0.6*j/N)

plotinit(0.4,0.14766)
plotinit(0.53,0.421)
plotinit(0.356497,0.345194)

nit=10000
k=0.97
def devV(q):
    return k/(2*np.pi)*np.sin(2*np.pi*q)
def plotinit(q0,p0):
    data=[np.array([q0,p0])]
    
    for i in range(nit-1):
        tmp=q0
        p0=p0+devV(q0)
        q0=q0+p0

        q0=(q0)%1
        p0=(p0+1)%1
        data.append(np.array([q0,p0]))
    np.array(data)
    data=np.transpose(data)
    plt.plot(data[0],data[1],'.',markersize=0.8)

    return
N=7
for j in range(N):
     
       plotinit(0.6,random.random())
plt.show()
