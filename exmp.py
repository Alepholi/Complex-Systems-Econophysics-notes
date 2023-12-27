import numpy as np
import matplotlib.pyplot as plt
import random
nit=10000
alpha=2*np.pi*0.25
beta=0.5
def plotinit(q0,p0):
    data=[np.array([q0,p0])]
    
    for i in range(nit-1):
        tmp=q0
        q0=q0*np.cos(alpha)-(p0-q0**2*beta)*np.sin(alpha)
        p0=(p0-tmp**2*beta)*np.cos(alpha)+tmp*np.sin(alpha)
        q0=(q0+1)%2-1
        p0=(p0+1)%2-1
        data.append(np.array([q0,p0]))
    np.array(data)
    data=np.transpose(data)
    plt.plot(data[0],data[1],'.',markersize=0.8)

    return
N=10
for j in range(N):
    plotinit(0,2*j/(1*N)-1)
    print(j/(2*N)-0.5)
#plotinit(0.4,0.3244)
#plotinit(0.795,0.1)
plotinit(-0.3,-0.3)
plotinit(0.9,-0.8)
plotinit(-0.32,-0.91)
plotinit(-0.66,-0.8)
plotinit(-0.8,-0.7)
plotinit(0.83,-0.9)
plotinit(-0.6,-0.5)

'''
ar=[]
for i in range(1000):
    x=random.random()-0.5
    y=0.2*np.sqrt(1-x*x/(0.25))*(-1)**i
    ar.append(np.array([x,y])) 
ar=np.transpose(ar)
plt.plot(ar[0],ar[1],'.')
ar2=(ar[1]-ar[0]**2+1)%2-1
plt.plot(ar[0],ar2,'.')
ar3=ar[0]*np.cos(alpha)-ar2*np.sin(alpha)
ar4=ar[0]*np.sin(alpha)+ar2*np.cos(alpha)
plt.plot(ar3,ar4,'.')
plt.axis("equal")'''
plt.show()
#print(ar)