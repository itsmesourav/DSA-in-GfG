class Solution:
    def maxDotProduct(self, a, b):
        n, m = len(a), len(b)
        NEG = float('-inf')

        prev = [NEG] * (m + 1)
        prev[0] = 0

        for i in range(1, n + 1):
            curr = [NEG] * (m + 1)
            curr[0] = 0
            for j in range(1, min(i, m) + 1):
                curr[j] = max(
                    prev[j],                              # Skip a[i-1]
                    prev[j - 1] + a[i - 1] * b[j - 1]    # Match
                )
            prev = curr

        return prev[m]