class Solution:
    def findPosition(self, n):
        # If n is zero or has more than one set bit
        if n <= 0 or (n & (n - 1)) != 0:
            return -1
        
        position = 1
        
        # Find position of the only set bit
        while n > 1:
            n >>= 1
            position += 1
        
        return position