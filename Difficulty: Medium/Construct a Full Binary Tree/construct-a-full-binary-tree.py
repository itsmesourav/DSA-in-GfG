'''
Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def constructBinaryTree(self, pre, preMirror):
        n = len(pre)
        pos = {val: i for i, val in enumerate(preMirror)}
        self.idx = 0

        def build(l, r):
            if self.idx >= n or l > r:
                return None

            root = Node(pre[self.idx])
            self.idx += 1

            if l == r or self.idx >= n:
                return root

            # Position of left child root in mirror preorder
            p = pos[pre[self.idx]]

            root.left = build(p, r)
            root.right = build(l + 1, p - 1)

            return root

        return build(0, n - 1)