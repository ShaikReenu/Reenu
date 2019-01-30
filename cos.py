import matplotlib.pyplot as mat
import numpy as num
x1=num.arange(0,5,0.02)
y1=num.cos(x1*2*num.pi)
mat.plot(x1,y1)
mat.title('cosine wave')
mat.xlabel('time')
mat.ylabel('amplitude')
mat.show( )
