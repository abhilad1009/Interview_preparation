"""
This problem was asked by Google.

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d

"""


class Node(object):
    def __init__(self, val, left=None,right=None):
        self.value = val
        self.left = left
        self.right = right

def deepest(node,lvl,Deep_node):
    if node.left==None and node.right==None:
        if Deep_node[1]<lvl:
            Deep_node[1]=lvl
            Deep_node[0]=node
            return
    else:
        if node.left:
            deepest(node.left,lvl+1,Deep_node)
        if node.right:
            deepest(node.right,lvl+1,Deep_node)

    return Deep_node


root=Node(1,Node(2,Node(3),Node(5,Node(7))),Node(4))

ans=deepest(root,0,[root,0])

print(ans[1])
print(ans[0].value)