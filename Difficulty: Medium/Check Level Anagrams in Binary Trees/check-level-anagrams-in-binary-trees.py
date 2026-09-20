class Solution:

    def areAnagrams(self, root1, root2):
        q1 = [root1]
        q2 = [root2]

        while q1 and q2:
            level1 = []
            level2 = []

            for node in q1:
                level1.append(node.data)

            for node in q2:
                level2.append(node.data)

            if sorted(level1) != sorted(level2):
                return False

            next1 = []
            next2 = []

            for node in q1:
                if node.left:
                    next1.append(node.left)
                if node.right:
                    next1.append(node.right)

            for node in q2:
                if node.left:
                    next2.append(node.left)
                if node.right:
                    next2.append(node.right)

            q1 = next1
            q2 = next2

        return not q1 and not q2