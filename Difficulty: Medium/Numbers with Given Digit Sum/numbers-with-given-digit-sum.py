class Solution:
    def countWays(self, n, sum):
        # Impossible cases
        if sum > 9 * n or sum < 1:
            return -1

        # dp[i][j] = ways to form sum j using i digits (0-9)
        dp = [[0] * (sum + 1) for _ in range(n)]
        dp[0][0] = 1

        for i in range(1, n):
            for s in range(sum + 1):
                for d in range(10):
                    if s >= d:
                        dp[i][s] += dp[i - 1][s - d]

        ans = 0
        for first in range(1, 10):
            if sum >= first:
                ans += dp[n - 1][sum - first]

        return ans if ans > 0 else -1