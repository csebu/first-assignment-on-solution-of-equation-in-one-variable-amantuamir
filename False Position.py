import math


def calc(x):
    return 3 * x + math.sin(x) - math.exp(x)

def FalsePos(a,b):
    while(abs(b-a)>0):
       if (calc(a)*calc(b)<0):
           m=((a*calc(b))-(b*calc(a)))/(calc(b)-calc(a))
       if (calc(m) == 0.0):
           break
       elif (calc(a) * calc(m)) < 0:
           b = m
       else:
           a = m
    print("The value of root is : ", "%.8f" % m)
A = 0
B = 1
FalsePos(A, B)
