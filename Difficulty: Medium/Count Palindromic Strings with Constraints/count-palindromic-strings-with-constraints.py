class Solution:
    def palindromicStrings(self, n, k):
        MOD = 10**9 + 7
        ans = 0
        perm = 1

        for m in range(k + 1):
            if m > 0 and 2 * m <= n:
                ans = (ans + perm) % MOD

            if 2 * m + 1 <= n:
                ans = (ans + (k - m) * perm) % MOD

            if m < k:
                perm = (perm * (k - m)) % MOD

        return ans