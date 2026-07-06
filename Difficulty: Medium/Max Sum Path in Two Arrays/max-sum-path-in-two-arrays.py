class Solution:
    def maxPathSum(self, a, b):
        i = j = 0
        sum1 = sum2 = 0
        ans = 0

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                sum1 += a[i]
                i += 1
            elif a[i] > b[j]:
                sum2 += b[j]
                j += 1
            else:
                ans += max(sum1, sum2) + a[i]
                sum1 = sum2 = 0
                i += 1
                j += 1

        while i < len(a):
            sum1 += a[i]
            i += 1

        while j < len(b):
            sum2 += b[j]
            j += 1

        ans += max(sum1, sum2)
        return ans