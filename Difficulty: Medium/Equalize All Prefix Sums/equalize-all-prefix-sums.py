class Solution:
    def optimalArray(self, arr):
        n = len(arr)
        ans = [0] * n

        for i in range(1, n):
            ans[i] = ans[i - 1] + arr[i] - arr[i // 2]

        return ans