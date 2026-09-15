class Solution:
    def getCount(self, root, k):
        if root is None:
            return 0

        leaf_levels = []
        queue = [(root, 1)]

        while queue:
            node, level = queue.pop(0)

            # Leaf node
            if node.left is None and node.right is None:
                leaf_levels.append(level)
                continue

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        # Visit cheapest leaves first
        leaf_levels.sort()

        total = 0
        count = 0

        for level in leaf_levels:
            if total + level > k:
                break

            total += level
            count += 1

        return count