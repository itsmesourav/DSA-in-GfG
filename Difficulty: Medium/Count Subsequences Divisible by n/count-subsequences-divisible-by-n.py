class Solution:
    def countSubsequences(self, s, n):
        MOD = 10**9 + 7
        dp = [0] * n

        for ch in s:
            d = int(ch)
            ndp = dp[:]  # subsequences that don't use this digit

            # Start a new subsequence with this digit
            ndp[d % n] = (ndp[d % n] + 1) % MOD

            # Append this digit to every existing subsequence
            for r in range(n):
                if dp[r]:
                    nr = (r * 10 + d) % n
                    ndp[nr] = (ndp[nr] + dp[r]) % MOD

            dp = ndp

        return dp[0]