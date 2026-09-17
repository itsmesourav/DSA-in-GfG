class Solution:
    def absDiff(self, root):
        prev = None
        ans = float('inf')

        def inorder(node):
            nonlocal prev, ans

            if node is None:
                return

            inorder(node.left)

            if prev is not None:
                ans = min(ans, node.data - prev)

            prev = node.data

            inorder(node.right)

        inorder(root)

        return ans