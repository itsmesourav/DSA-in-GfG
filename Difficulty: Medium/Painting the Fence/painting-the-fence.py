class Solution:
    def countWays(self, n, k):
        if n == 1:
            return k
        
        same = k        # for n = 2 → same = k
        diff = k * (k - 1)
        
        for _ in range(3, n + 1):
            new_same = diff
            new_diff = (same + diff) * (k - 1)
            
            same, diff = new_same, new_diff
        
        return same + diff