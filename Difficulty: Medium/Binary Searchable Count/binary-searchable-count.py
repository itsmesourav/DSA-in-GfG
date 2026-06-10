class Solution:
    def binarySearchable(self, arr):
        n = len(arr)
        ans = 0

        stack = [(0, n - 1, float('-inf'), float('inf'))]

        while stack:
            l, r, low, high = stack.pop()

            if l > r:
                continue

            mid = (l + r) // 2
            val = arr[mid]

            if low < val < high:
                ans += 1

            stack.append((l, mid - 1, low, min(high, val)))
            stack.append((mid + 1, r, max(low, val), high))

        return ans