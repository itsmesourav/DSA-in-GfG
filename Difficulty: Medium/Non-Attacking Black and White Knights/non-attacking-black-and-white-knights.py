class Solution:
    def numOfWays(self, n, m):
        N = n * m

        total = N * (N - 1)

        attacking = 4 * (
            max(0, n - 1) * max(0, m - 2) +
            max(0, n - 2) * max(0, m - 1)
        )

        return total - attacking