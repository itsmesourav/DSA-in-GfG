class Solution:
    def countStrings(self, n, k):
        MOD = 10**9 + 7

        # dp[length][adjacent_11_count][last_bit]
        dp = [[[0] * 2 for _ in range(k + 2)] for _ in range(n + 1)]

        # Base case: strings of length 1
        dp[1][0][0] = 1
        dp[1][0][1] = 1

        for i in range(2, n + 1):
            for j in range(k + 1):
                # Append 0
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD

                # Append 1 after 0
                dp[i][j][1] = (dp[i][j][1] + dp[i - 1][j][0]) % MOD

                # Append 1 after 1 (creates one more adjacent "11")
                if j > 0:
                    dp[i][j][1] = (dp[i][j][1] + dp[i - 1][j - 1][1]) % MOD

        return (dp[n][k][0] + dp[n][k][1]) % MOD