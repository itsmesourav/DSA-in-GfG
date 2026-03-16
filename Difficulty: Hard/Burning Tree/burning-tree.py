'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def find_node(self, root, target, parent):
        if not root:
            return
        
        if root.data == target:
            self.node = root
            
        self.parent[root] = parent
        self.find_node(root.left, target, root)
        self.find_node(root.right, target, root)
        
    def minTime(self, root, target):
        self.parent = dict()
        self.node = None
        
        self.find_node(root, target, None)
        
        q = deque([(self.node, 0)])
        visited = dict()
        ans = 0
        
        while len(q):
            root, color_num = q.popleft()
            ans = color_num
            
            if root.left and  root.left not in visited:
                q.append((root.left, color_num + 1))
                
            if root.right and root.right not in visited:
                q.append((root.right, color_num + 1))
            
            if self.parent[root] and self.parent[root] not in visited:
                q.append((self.parent[root], color_num + 1))
                
            visited[root] = True
        return ans
        
        
