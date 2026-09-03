class Solution:
    def maxDiffSum(self, arr):
        n = len(arr)
        keep = 0
        one = 0

        for i in range(1, n):
            new_keep = max(
                keep + abs(arr[i] - arr[i - 1]),
                one + abs(arr[i] - 1)
            )

            new_one = max(
                keep + abs(1 - arr[i - 1]),
                one + abs(1 - 1)
            )

            keep, one = new_keep, new_one

        return max(keep, one)