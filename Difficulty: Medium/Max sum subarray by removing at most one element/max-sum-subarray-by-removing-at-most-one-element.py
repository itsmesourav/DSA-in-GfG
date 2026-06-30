class Solution:
    def maxSumSubarray(self, arr):
        keep = arr[0]          # Max sum ending here without deletion
        delete = float('-inf') # Max sum ending here with one deletion
        ans = arr[0]

        for i in range(1, len(arr)):
            prev_keep = keep

            keep = max(arr[i], keep + arr[i])
            delete = max(prev_keep, delete + arr[i])

            ans = max(ans, keep, delete)

        return ans