import matplotlib.pyplot as mtpt
import numpy as ny
t=ny.arange(0,10,0.01)
x1=ny.sin(t*2*ny.pi)
mtpt.plot(t,x1)
mtpt.title('sine wave')
mtpt.xlabel('time')
mtpt.ylabel('amplitude')
mtpt.show( )

