class Solution:

    def maxTask(self, h: list[int], l: list[int]) -> int:

        n = len(h)

        if n == 1:
            return max(h[0], l[0])

        dp = [0] * n

        # Day 0
        dp[0] = max(h[0], l[0])

        # Day 1
        dp[1] = max(
            dp[0] + l[1],
            h[1]
        )

        # Remaining days
        for i in range(2, n):
            dp[i] = max(
                dp[i - 1],          # do nothing
                dp[i - 1] + l[i],   # low effort
                dp[i - 2] + h[i]    # high effort
            )

        return dp[n - 1]