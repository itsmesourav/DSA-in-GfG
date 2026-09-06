class Solution:
    def pairAndSum(self, arr):
        ans = 0
        
        for bit in range(31):
            cnt = 0
            
            for x in arr:
                if x & (1 << bit):
                    cnt += 1
                    
            ans += (cnt * (cnt - 1) // 2) * (1 << bit)
        
        return ans