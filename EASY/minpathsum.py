"""
This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1
"""
import math
class Node(object):
    def __init__(self,val,left=None,right=None):
        self.value=val
        self.left=left
        self.right=right


def minpathsum(node,currsum):
    # print(node.value)
    if node.left==None and node.right==None:
        return currsum+node.value
    leftsum,rightsum=math.inf,math.inf
    if node.left:
        leftsum=minpathsum(node.left,currsum+node.value)
        # print(leftsum)
    if node.right:
        rightsum=minpathsum(node.right,currsum+node.value)
        # print(rightsum)

    if leftsum<rightsum:
        return leftsum
    else:
        return rightsum


root=Node(10,Node(5,None,Node(-4,Node(3),)),Node(5,None,Node(1,None,Node(-1))))

ans=minpathsum(root,0)
print(ans)