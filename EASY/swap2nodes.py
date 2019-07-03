"""
This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4 -> 5 -> 6, return 2 -> 1 -> 4 -> 3 -> 6 -> 5.

"""

class Node(object):
    def __init__(self,val,next=None):
        self.value=val
        self.next=next

def swaptwo(node):
    
    if node.next==None:
        return node
    prev=node
    curr=node.next.next
    head=node.next
    head.next=prev
    while curr and curr.next:
        prev.next=curr.next
        prev=curr
        next=curr.next.next
        curr.next.next=curr
        curr=next
    
    prev.next=curr
    
    return head



n1=Node(4)
n2=Node(3,n1)
n3=Node(2,n2)
head=Node(1,n3)
# head=Node(5,n4)

ans=swaptwo(head)
while ans:
    print(ans.value)
    ans=ans.next