class Solution:
    def minCost(self, n: int, i: int, d: int, c: int) -> int:
        dp = [0] + [float('inf')] * n

        for x in range(1, n + 1):
            dp[x] = dp[x - 1] + i

            if x % 2 == 0:
                dp[x] = min(dp[x], dp[x // 2] + c)
            else:
                if x > 1:
                    dp[x] = min(dp[x], dp[(x + 1) // 2] + c + d)

        return dp[n]