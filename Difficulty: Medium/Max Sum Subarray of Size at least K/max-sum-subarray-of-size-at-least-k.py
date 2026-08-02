class Solution:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        n = len(arr)

        # Kadane: max subarray sum ending at each index
        max_end = [0] * n
        max_end[0] = arr[0]

        for i in range(1, n):
            max_end[i] = max(arr[i], max_end[i - 1] + arr[i])

        # First window of size k
        window_sum = sum(arr[:k])
        ans = window_sum

        # Slide the window
        for i in range(k, n):
            window_sum += arr[i] - arr[i - k]

            # Window alone
            ans = max(ans, window_sum)

            # Extend window with best prefix ending before it
            ans = max(ans, window_sum + max_end[i - k])

        return ans