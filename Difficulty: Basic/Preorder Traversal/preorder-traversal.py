class Solution:
    def preOrder(self, root):
        ans = []

        def dfs(node):
            if not node:
                return
            ans.append(node.data)   # Visit root
            dfs(node.left)          # Traverse left
            dfs(node.right)         # Traverse right

        dfs(root)
        return ans