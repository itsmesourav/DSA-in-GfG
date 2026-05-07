# Definition for Node
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Solution:
    
    # Function to check if two trees are identical
    def isIdentical(self, root1, root2):
        
        # If both are None
        if root1 is None and root2 is None:
            return True
        
        # If one is None and the other is not
        if root1 is None or root2 is None:
            return False
        
        # Check current node and subtrees
        return (root1.data == root2.data and
                self.isIdentical(root1.left, root2.left) and
                self.isIdentical(root1.right, root2.right))
    
    def isSubTree(self, root1, root2):
        
        # Empty tree is always a subtree
        if root2 is None:
            return True
        
        # If main tree becomes empty
        if root1 is None:
            return False
        
        # If trees match from current node
        if self.isIdentical(root1, root2):
            return True
        
        # Otherwise check left and right subtree
        return (self.isSubTree(root1.left, root2) or
                self.isSubTree(root1.right, root2))