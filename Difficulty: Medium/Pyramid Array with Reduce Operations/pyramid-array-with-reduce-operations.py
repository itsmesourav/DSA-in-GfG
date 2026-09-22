class Solution:
    def formPyramid(self, arr):
        n = len(arr)
        left = [0] * n
        right = [0] * n

        left[0] = 1
        for i in range(1, n):
            left[i] = min(arr[i], left[i - 1] + 1)

        right[n - 1] = 1
        for i in range(n - 2, -1, -1):
            right[i] = min(arr[i], right[i + 1] + 1)

        total = sum(arr)
        max_sum = 0

        for i in range(n):
            peak = min(left[i], right[i])
            max_sum = max(max_sum, peak * peak)

        return total - max_sum