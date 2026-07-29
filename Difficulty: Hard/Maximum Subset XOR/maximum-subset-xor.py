class Solution:
    def maxSubsetXOR(self, arr):
        n = len(arr)
        index = 0

        for bit in range(31, -1, -1):
            max_idx = -1

            for i in range(index, n):
                if arr[i] & (1 << bit):
                    max_idx = i
                    break

            if max_idx == -1:
                continue

            arr[index], arr[max_idx] = arr[max_idx], arr[index]

            for i in range(n):
                if i != index and (arr[i] & (1 << bit)):
                    arr[i] ^= arr[index]

            index += 1

        ans = 0
        for x in arr:
            ans = max(ans, ans ^ x)

        return ans