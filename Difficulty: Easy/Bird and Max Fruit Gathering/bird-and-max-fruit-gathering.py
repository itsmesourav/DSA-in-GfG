class Solution:

    def maxFruits(self, arr: list[int], m: int) -> int:
        n = len(arr)
        
        window_sum = sum(arr[:m])
        ans = window_sum
        
        for i in range(m, m + n - 1):
            window_sum += arr[i % n]
            window_sum -= arr[(i - m) % n]
            ans = max(ans, window_sum)
        
        return ans