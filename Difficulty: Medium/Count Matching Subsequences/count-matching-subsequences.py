class Solution:
    def countWays(self, s1, s2):
        MOD = 10**9 + 7

        n = len(s1)
        m = len(s2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Empty s2 can always be formed
        for i in range(n + 1):
            dp[i][m] = 1

        # Fill table from back
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = (dp[i + 1][j + 1] + dp[i + 1][j]) % MOD
                else:
                    dp[i][j] = dp[i + 1][j]

        return dp[0][0]