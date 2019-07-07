"""
This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1

"""


class Node(object):

    def __init__(self,val):
        self.val=val
        self.next=None


def getlist(num):
    start=Node(num%10)
    curr=start
    num=num//10
    while num:
        curr.next=Node(num%10)
        num=num//10
        curr=curr.next

    return start

def getnum(node):
    i=0
    num=0
    num+=((10**i)*node.val)
    i+=1
    node=node.next
    while node:
        num += ((10**i)*node.val)
        i+=1
        node=node.next
    return num


def getsum(L1,L2):
    tmpsum=0
    tmpsum+=L1.val+L2.val
    start=Node(tmpsum%10)
    curr=start
    tmpsum=tmpsum//10
    L1=L1.next
    L2=L2.next
    while tmpsum or L1 or L2:
        if L1:
            tmpsum+=L1.val
            L1=L1.next
        if L2:
            tmpsum+=L2.val
            L2=L2.next

        curr.next=(Node(tmpsum%10))
        curr=curr.next
        tmpsum=tmpsum//10

    return start

N=getlist(54321)
while N:
    print(N.val)
    N=N.next

N=getlist(345)
print(getnum(N))

L1=getlist(99)
L2=getlist(25)
L3=getsum(L1,L2)

print(getnum(L3))