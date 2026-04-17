class Solution:
    def maxOnes(self, arr):
        total_ones = sum(arr)
        
        max_gain = 0
        current = 0
        
        for x in arr:
            value = 1 if x == 0 else -1
            current = max(value, current + value)
            max_gain = max(max_gain, current)
            
        return total_ones + max_gain