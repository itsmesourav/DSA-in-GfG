class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:
        n = len(arr)

        if k == 0:
            return max(arr) - min(arr)

        size = n - k

        prefix_min = [0] * n
        prefix_max = [0] * n
        suffix_min = [0] * n
        suffix_max = [0] * n

        prefix_min[0] = prefix_max[0] = arr[0]

        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i - 1], arr[i])
            prefix_max[i] = max(prefix_max[i - 1], arr[i])

        suffix_min[n - 1] = suffix_max[n - 1] = arr[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], arr[i])
            suffix_max[i] = max(suffix_max[i + 1], arr[i])

        ans = float('inf')

        for start in range(n - k + 1):
            end = start + k
            low = float('inf')
            high = float('-inf')

            if start > 0:
                low = min(low, prefix_min[start - 1])
                high = max(high, prefix_max[start - 1])

            if end < n:
                low = min(low, suffix_min[end])
                high = max(high, suffix_max[end])

            if low != float('inf'):
                ans = min(ans, high - low)
            else:
                return 0

        return ans