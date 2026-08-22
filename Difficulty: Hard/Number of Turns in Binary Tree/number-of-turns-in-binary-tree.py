''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    
    def numberOfTurns(self, root, p, q):
        def get_path(node, target, path):
            if not node:
                return False

            if node.data == target:
                return True

            path.append('L')
            if get_path(node.left, target, path):
                return True
            path.pop()

            path.append('R')
            if get_path(node.right, target, path):
                return True
            path.pop()

            return False

        path_p = []
        path_q = []

        get_path(root, p, path_p)
        get_path(root, q, path_q)

        i = 0
        while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
            i += 1

        # Build complete direction sequence from p to q
        # Reverse p's path after LCA, then follow q's path.
        route = path_p[i:][::-1] + path_q[i:]

        turns = 0
        for j in range(1, len(route)):
            if route[j] != route[j - 1]:
                turns += 1

        return turns if turns > 0 else -1