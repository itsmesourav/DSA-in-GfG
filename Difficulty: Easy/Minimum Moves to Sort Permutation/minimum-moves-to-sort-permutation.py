class Solution:
    def minMoves(self, arr):
        n = len(arr)

        pos = [0] * (n + 1)

        for i, x in enumerate(arr):
            pos[x] = i

        longest = 1
        curr = 1

        for x in range(1, n):
            if pos[x] < pos[x + 1]:
                curr += 1
            else:
                curr = 1

            longest = max(longest, curr)

        return n - longest