class Solution:
    def maximumSubarray(self, arr: list[int]) -> int:
        a = arr[0]
        b = arr[0] * arr[0]
        ans = b

        for x in arr[1:]:
            p = a
            q = b

            a = max(x, p + x)
            b = max(x * x, p + x * x, q + x)

            ans = max(ans, a, b)

        return ans