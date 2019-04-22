import matplotlib.pyplot as mp
import numpy as np
import cmath as m
x=[5,3,1,1,2]
j=m.sqrt(-1)
X=[]
for n in range(0,len(x)):
	s=0
	for k in range(0,(len(x)-1)):
		s=s+(x[k]*np.exp(-j*2*np.pi*k*n/2))
	X=np.append(X,s)
mp.plot(X)
mp.title("DFT")
mp.show()

	