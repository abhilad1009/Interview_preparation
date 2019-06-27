"""
This problem was asked by Two Sigma.

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, 
implement a function rand5() that returns an integer from 1 to 5 (inclusive).

"""

import random

def rand7():
    return random.randint(1,7)

def rand5():
    result=rand7()
    if result>5:
        result=rand5()
    return result

d={1:0,2:0,3:0,4:0,5:0}


for i in range(100000):
    d[rand5()]+=1

print(d)
