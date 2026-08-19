class Solution:
    def maxDiff(self, root):
        ans = float('-inf')

        def dfs(node):
            nonlocal ans

            if not node:
                return float('inf')

            left_min = dfs(node.left)
            right_min = dfs(node.right)

            # Minimum descendant value
            min_desc = min(left_min, right_min)

            if min_desc != float('inf'):
                ans = max(ans, node.data - min_desc)

            # Minimum value in this subtree
            return min(node.data, min_desc)

        dfs(root)
        return ans