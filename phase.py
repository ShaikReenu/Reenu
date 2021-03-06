import matplotlib.pyplot as pyplot
import numpy as num
fs=int(input("enter the sampling frequency"))
f1=int(input("enter the first frequency"))
f2=int(input("enter the second frequency"))
n=int(input("enter the sample rate"))
p1=int(input("enter the first phase"))
p2=int(input("enter the second phase"))
x=num.arange(n)
x1=num.cos((2*num.pi*f1/fs*x)+p1)
pyplot.subplot(3,1,1)
pyplot.plot(x,x1)
pyplot.xlabel('---->samples')
pyplot.ylabel('---->amplitude')
x2=num.cos((2*num.pi*f2/fs*x)+p2)
pyplot.subplot(3,1,2)
pyplot.plot(x,x2)
pyplot.xlabel('---->samples')
pyplot.ylabel('---->amplitude')
y=x1+x2
pyplot.subplot(3,1,3)
pyplot.plot(x,y)
pyplot.title('sample o/p')
pyplot.show( )
