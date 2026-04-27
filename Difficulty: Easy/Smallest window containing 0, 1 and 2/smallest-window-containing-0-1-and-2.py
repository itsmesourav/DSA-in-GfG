class Solution:
    def smallestSubstring(self, s):
        cnt = {'0':0, '1':0, '2':0}
        l = 0
        ans = float('inf')
        
        for r in range(len(s)):
            cnt[s[r]] += 1
            
            while cnt['0'] > 0 and cnt['1'] > 0 and cnt['2'] > 0:
                ans = min(ans, r - l + 1)
                cnt[s[l]] -= 1
                l += 1
        
        return ans if ans != float('inf') else -1