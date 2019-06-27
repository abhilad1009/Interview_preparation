"""
The problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +   +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).


"""

class Node(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def evaluate(root):

    if type(root.val) is int:
        return root.val
    if root.val == '+':
        return evaluate(root.left)+evaluate(root.right)
    if root.val == '-':
        return evaluate(root.left)-evaluate(root.right)
    if root.val == '*':
        return evaluate(root.left)*evaluate(root.right)
    if root.val == '/':
        return evaluate(root.left)/evaluate(root.right)


if __name__ == "__main__":
    root = Node('*', Node('/', Node(3), Node(2)),
                Node('+', Node('*', Node(2), Node(5)), Node(5)))
    print(evaluate(root))
