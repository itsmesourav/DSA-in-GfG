class Solution:
    def toSumTree(self, root):
        
        def solve(node):
            if not node:
                return 0
            
            # Store original value
            old_val = node.data
            
            # Recursively get sum of left and right subtrees
            left_sum = solve(node.left)
            right_sum = solve(node.right)
            
            # Update current node value
            node.data = left_sum + right_sum
            
            # Return total sum including original node value
            return node.data + old_val
        
        solve(root)