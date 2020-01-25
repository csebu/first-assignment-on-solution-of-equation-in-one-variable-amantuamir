
import math


def func(x):
    return 3 * x + math.sin(x) - math.exp(x)
def calc(x):
    return 3  + math.cos(x) - math.exp(x)

def newton(a,b) :
    if (func(a) * func(b) < 0):
        m = (a + b) / 2
    else:
        print("Root is not here.")
    while (calc(m) > 0):
        h=func(m)/calc(m)
        if(h==0.0):
            break
        m=m-h
    print("The value of root is : ", "%.8f" % m)
A=0
B=0.5
newton(A, B)
