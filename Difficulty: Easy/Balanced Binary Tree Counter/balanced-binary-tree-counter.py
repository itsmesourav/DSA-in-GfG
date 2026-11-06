class Solution:
    def countBT(self, h: int) -> int:
        mod = 10**9 + 7
        
        if h == 1:
            return 1
        if h == 2:
            return 3
        
        a = 1
        b = 3
        
        for i in range(3, h + 1):
            c = (b * (2 * a + b)) % mod
            a = b
            b = c
        
        return b