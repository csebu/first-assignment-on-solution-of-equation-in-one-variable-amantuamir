import math

def calc(x):
    return 3 * x + math.sin(x) - math.exp(x)

def bisection(a,b):
    while(abs(b-a)>=0):
        m = (a + b) / 2
        if (calc(m) == 0.0):
            break
        if(calc(a)*calc(m))<0:
            b=m
        else:
            a=m
    print("The value of root is : ", "%.8f" % m)
A = 0.35
B = 0.38
bisection(A, B)
