"""
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.

"""
import math
def maxprod_1(L):
    L.sort()
    return max(L[0]*L[1]*L[-1],L[-1]*L[-2]*L[-3])

def maxprod_2(L):
    max1, max2, max3 = -math.inf, -math.inf, -math.inf
    min1, min2 = math.inf, math.inf

    for i in L:
        if i>max1:
            max3=max2
            max2=max1
            max1=i
        elif i>max2:
            max3=max2
            max2=i
        elif i>max3:
            max3=i

        if i<min1:
            min2=min1
            min1=i
        elif i<min2:
            min2=i
    
    return max(max1*max2*max3,max1*min1*min2)


L=[-40,-5,2,30]
print(maxprod_1(L))
print(maxprod_2(L))
