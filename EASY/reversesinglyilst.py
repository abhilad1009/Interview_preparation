"""
This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.

"""

class Node(object):
    def __init__(self,val,nxt=None):
        self.value=val
        self.next=nxt

# h->4->3->2->1

def inplace_reverse(head):
    curr=head
    oldnext=curr.next
    newnext=None
    while curr:
        curr.next=newnext
        newnext=curr
        curr=oldnext
        try:
            oldnext=curr.next
        except:
            continue
    return newnext





n1=Node(1)
n2=Node(2,n1)
n3=Node(3,n2)
n4=Node(4,n3)
head=Node(5,n4)


new_head=inplace_reverse(head)
print(new_head)
N=new_head
while N:
    print(N.value)
    N=N.next

