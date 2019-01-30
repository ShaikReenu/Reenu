import matplotlib.pyplot as mp
import numpy as np
t=np.arange(0,15,0.05)
x1=np.sin(2*np.pi*t)
mp.subplot(1,3,1)
mp.plot(t,x1)
mp.title('sinwave')
mp.xlabel('---->time')
mp.ylabel('---->amplitude')
x2=np.cos(2*np.pi*t)
mp.subplot(1,3,2)
mp.plot(t,x2)
mp.title('cos wave')
mp.xlabel('----->time')
mp.ylabel('----->amplitude')
z=x1+x2
mp.subplot(1,3,3)
mp.plot(t,z)
mp.title('addition of sin and cos')
mp.xlabel('---->time')
mp.ylabel('---->amplitude')
mp.show( )


