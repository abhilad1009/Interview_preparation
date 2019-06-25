"""
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.

"""
import math

def perfectnum(n):
    nthelement=19+(n-1)*9
    outlier=int(math.log10(nthelement))-1
    nthelement+=9*outlier
    return nthelement

print(perfectnum(10))
