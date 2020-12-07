from math import sqrt
from statistics import *
def heron(a, b, c):
    data = a,b,c
    if(max(data) >= min(data) + median(data)):
        print("Not a triangle")
        return
    s = (a+b+c)/2
    result = sqrt(s*(s-a)*(s-b)*(s-c))
    print(result)

heron(5,10,15)