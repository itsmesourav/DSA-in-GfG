class Solution:
    def minToggle(self, arr):
        n = len(arr)

        # Prefix count of 1s
        prefix_ones = [0] * (n + 1)

        for i in range(n):
            prefix_ones[i + 1] = prefix_ones[i] + (1 if arr[i] == 1 else 0)

        total_zeros = arr.count(0)
        ans = float('inf')

        # Try every partition point
        for i in range(n + 1):
            # Left side should be all 0s -> toggle 1s to 0s
            left_cost = prefix_ones[i]

            # Right side should be all 1s -> toggle 0s to 1s
            zeros_right = total_zeros - (i - prefix_ones[i])
            right_cost = zeros_right

            ans = min(ans, left_cost + right_cost)

        return ans