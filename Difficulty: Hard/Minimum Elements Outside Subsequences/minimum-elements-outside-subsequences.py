class Solution:
    def minCount(self, arr):
        n = len(arr)
        dp = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]

        def solve(pos, inc, dec):
            if pos == n:
                return 0

            i, d = inc + 1, dec + 1
            if dp[pos][i][d] != -1:
                return dp[pos][i][d]

            ans = solve(pos + 1, inc, dec)

            if inc == -1 or arr[pos] > arr[inc]:
                ans = max(ans, 1 + solve(pos + 1, pos, dec))

            if dec == -1 or arr[pos] < arr[dec]:
                ans = max(ans, 1 + solve(pos + 1, inc, pos))

            dp[pos][i][d] = ans
            return ans

        return n - solve(0, -1, -1)