class Solution:
    def firstElementKTime(self, arr: list[int], k: int) -> int:
        d = {}
        
        for i in arr:
            d[i] = d.get(i, 0) + 1
            
            if d[i] == k:
                return i
        
        return -1