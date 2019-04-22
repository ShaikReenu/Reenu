import matplotlib.pyplot as mp
import numpy as nm
import math as m
#implementing the butterworth lowpassfilter
pg=int(input("enter the pass band gain in db:"))
sg=int(input("enter the stop band gain in db:"))
wp=int(input("enter the pass band frequency:"))
ws=int(input("enter the stop band frequency:"))
#order of the filter given as 'N'
n1=1/sg**2
n2=1/pg**2
n=0.5*nm.log(n1/n2)
N=n/nm.log10(ws/wp)
w=nm.linspace(0,8000,8000)
#finding the cut of frequency as wc
wc=wp/((1/wp**2)-1)**0.5*N
#applying the butterworth filter |H(jw)| as h
h1=1+(w/wc)**2*N
h2=nm.sqrt(h1)
h=1/h2
mp.plot(w,h)
mp.grid()
mp.show()