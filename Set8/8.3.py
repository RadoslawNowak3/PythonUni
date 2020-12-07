from random import *
from math import sqrt
inside=0
n=10**7
seed()
for i in range(0,n):
    x=random()
    y=random()
    if sqrt(y*y+x*x)<=1:
        inside+=1
pi=4*inside/n
print ("Pi = ",pi)