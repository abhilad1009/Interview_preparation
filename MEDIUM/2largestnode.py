"""
This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.
"""
import math

class Node(object):
    def __init__(self,val):
        self.value=val
        self.left=None
        self.right=None

def insert(root,val):
    if root.value>val:
        if root.left==None:
            root.left=Node(val)
        else:
            insert(root.left,val)
    else:
        if root.right==None:
            root.right=Node(val)
        else:
            insert(root.right,val)

def search2largest(root):
    L=[root]
    First=Node(-math.inf)
    Second=Node(-math.inf)
    while L!=[]:
        tmp=L.pop(0)
        if tmp.value>First.value:
            Second=First
            First=tmp
        elif tmp.value>Second.value:
            Second=tmp
        if tmp.left!=None:
            L.append(tmp.left)
        if tmp.right!=None:
            L.append(tmp.right)
    return First,Second

root=Node(6)
insert(root,2)
insert(root,4)
insert(root,8)
insert(root,5)
insert(root,7)
insert(root,9)
insert(root,10)

First,Second=search2largest(root)
print(First.value)
print(Second.value)
