import matplotlib.pyplot as mp
import numpy as nm
def movavg(x):
	p=int(input("enter the order of the moving system:"))
	n=len(x)
	z=[]
	for i in range(n):
		sum=0
		for k in range(p):
			if(i-k<n and i-k>=0):
				sum=sum+x[i-k]
		y=float(sum)/float(p)
		z=nm.append(z,y)
	return(z)
x=[]
g=int(input("enter the no.of samples:"))
for j in range(g):
	sum=int(input("enter the samples:"))
	x=nm.append(x,sum)
print("entered samples are:",x)
output=movavg(x)
print("output is:",output)
f1=int(input("enter the signal frequency:"))
f2=int(input("enter the sampling frequency:"))
x1=nm.arange(0,100,0.1)
y1=nm.sin(2*nm.pi*(float(f1)/float(f2)*x1))
mp.subplot(411)
mp.plot(y1)
N=nm.random.rand (y1. shape[0])
mp.subplot(412)
mp.plot(N)
y2=y1+N
mp.subplot(413)
mp.plot(y2)
d=movavg(y2)
mp.subplot(414)
mp.plot(d)
mp.xlabel("---->samples")
mp.ylabel("--->amplitude")
mp.show()


