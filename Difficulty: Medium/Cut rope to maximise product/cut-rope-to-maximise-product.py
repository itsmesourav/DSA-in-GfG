class Solution:
    def maxProduct(self, n):
        # Base Cases
        if n == 2:
            return 1
        if n == 3:
            return 2
            
        # Mathematical approach for n > 3
        remainder = n % 3
        
        # Case 1: Perfectly divisible by 3
        if remainder == 0:
            return 3 ** (n // 3)
            
        # Case 2: Remainder is 1 (e.g., n = 4 -> 2 * 2 = 4)
        elif remainder == 1:
            return (3 ** ((n // 3) - 1)) * 4
            
        # Case 3: Remainder is 2 (e.g., n = 5 -> 3 * 2 = 6)
        else:
            return (3 ** (n // 3)) * 2