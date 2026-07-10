class Solution:
    def getCount(self, n):
        count = 0 
        k = 2
        
        while k * (k + 1) // 2 <= n:
            rem = n - k * (k - 1) // 2
            if rem > 0 and rem % k == 0:
                count += 1
            k += 1
            
        return count