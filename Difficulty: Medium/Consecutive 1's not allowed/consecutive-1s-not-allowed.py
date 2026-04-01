class Solution:
    def countStrings(self, n):
        if n == 1:
            return 2
        
        a = 1  # ending with 0
        b = 1  # ending with 1
        
        for _ in range(2, n + 1):
            new_a = a + b
            new_b = a
            
            a, b = new_a, new_b
        
        return a + b