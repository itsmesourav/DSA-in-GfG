from collections import defaultdict

class Solution:
    def verticalSum(self, root):
        # Dictionary to store sum for each vertical line
        mp = defaultdict(int)

        # DFS traversal
        def solve(node, hd):
            if not node:
                return
            
            # Add current node value to its horizontal distance
            mp[hd] += node.data

            # Left child => hd - 1
            solve(node.left, hd - 1)

            # Right child => hd + 1
            solve(node.right, hd + 1)

        solve(root, 0)

        # Return sums from leftmost to rightmost
        return [mp[key] for key in sorted(mp)]