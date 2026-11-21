class Solution:
    def longestSubarrayDivK(self, arr, k):
        prefix_sum = 0
        first_seen = {0: -1}
        max_length = 0

        for i in range(len(arr)):
            prefix_sum += arr[i]

            remainder = prefix_sum % k

            if remainder in first_seen:
                max_length = max(max_length, i - first_seen[remainder])
            else:
                first_seen[remainder] = i

        return max_length