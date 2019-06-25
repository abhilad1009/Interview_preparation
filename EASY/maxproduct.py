"""
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.

"""
import math
def maxprod(L):
    L.sort()
    prod=-math.inf
    if L[-1]>=0:
        if L[0]<0 and L[1]<0:
            prod=L[0]*L[1]
        if L[-2]*L[-3]>prod:
            prod=L[-2]*L[-3]
        prod*=L[-1]
    else:
        prod=L[-1]*L[-2]*L[-3]
    return prod

L=[-40,-5,-2,-30]
print(maxprod(L))