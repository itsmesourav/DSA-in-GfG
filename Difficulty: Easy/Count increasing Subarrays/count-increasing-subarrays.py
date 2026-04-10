class Solution:
    def countIncreasing(self, arr):
        n = len(arr)
        if n < 2:
            return 0 
        
        
        count = 0
        length = 1
        
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                length += 1
                count += (length - 1)
            else:
                length = 1
        
        return count