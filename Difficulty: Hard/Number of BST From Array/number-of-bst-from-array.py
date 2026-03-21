class Solution:
    def countBSTs(self, arr):
        n = len(arr)
        MOD = 10**9+7
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n+1):
            for j in range(1, n+1):
                dp[i] = (dp[i] + dp[j-1]*dp[i-j])%MOD
        mp = {x: i for i, x in enumerate(sorted(arr))}
        result = [0]*n
        for i, e in enumerate(arr):
            left = mp[e]
            right = n - mp[e] - 1
            result[i] = (dp[left] * dp[right] % MOD)
        return result
