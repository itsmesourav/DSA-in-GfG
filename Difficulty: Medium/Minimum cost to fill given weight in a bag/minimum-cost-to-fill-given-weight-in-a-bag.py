class Solution:
    def minimumCost(self, cost, w):
        INF = float('inf')
        dp = [INF] * (w + 1)
        dp[0] = 0

        n = len(cost)

        for i in range(n):
            if cost[i] == -1:
                continue

            wt = i + 1
            c = cost[i]

            for j in range(wt, w + 1):
                dp[j] = min(dp[j], dp[j - wt] + c)

        return -1 if dp[w] == INF else dp[w]