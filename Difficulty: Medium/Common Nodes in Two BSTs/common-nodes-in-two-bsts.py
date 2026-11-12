class Solution:
    def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:
        s1, s2 = [], []
        ans = []

        while r1 or r2 or s1 or s2:

            while r1:
                s1.append(r1)
                r1 = r1.left

            while r2:
                s2.append(r2)
                r2 = r2.left

            if not s1 or not s2:
                break

            a = s1[-1].data
            b = s2[-1].data

            if a == b:
                ans.append(a)
                r1 = s1.pop().right
                r2 = s2.pop().right

            elif a < b:
                r1 = s1.pop().right

            else:
                r2 = s2.pop().right

        return ans