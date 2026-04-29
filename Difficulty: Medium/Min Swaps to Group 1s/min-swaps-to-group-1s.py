class Solution:
    def minSwaps(self, arr):
        k = sum(arr)  # total number of 1s
        
        # edge case
        if k == 0:
            return -1
        
        if k == 1:
            return 0
        
        curr = sum(arr[:k])
        max_ones = curr
        
        for i in range(k, len(arr)):
            curr += arr[i] - arr[i - k]
            max_ones = max(max_ones, curr)
        
        return k - max_ones