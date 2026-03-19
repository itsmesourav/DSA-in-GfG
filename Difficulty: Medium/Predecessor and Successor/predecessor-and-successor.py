'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def findPreSuc(self, root, key):
        pre = None
        suc = None
        
        while root:
            if root.data < key:
                pre = root
                root = root.right
            elif root.data > key:
                suc = root
                root = root.left
            else:
                
                if root.left:
                    temp = root.left
                    while temp.right:
                        temp = temp.right
                    pre = temp
                    
                if root.right:
                    temp = root.right
                    while temp.left:
                        temp = temp.left
                    suc = temp
                    
                break
        return pre, suc
