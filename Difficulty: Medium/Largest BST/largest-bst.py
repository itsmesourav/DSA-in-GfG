class Solution:
    def largestBst(self, root):
        self.max_size = 0
        
        def dfs(node):
            if not node:
                return (True, 0, float('inf'), float('-inf'))
                
            left_is_bst, left_size, left_min, left_max = dfs(node.left)
            right_is_bst, right_size, right_min, right_max = dfs(node.right)
                
            if left_is_bst and right_is_bst and left_max < node.data < right_min:
                size = left_size + right_size + 1
                self.max_size = max(self.max_size, size)
                return (
                    True,
                    size,
                    min(left_min, node.data),
                    max(right_max, node.data)
                    )
                        
            return (False, 0, 0, 0)
                
        dfs(root)
        return self.max_size
