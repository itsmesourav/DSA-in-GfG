class Solution:
    def levelSort(self, arr):
        ans = []
        i = 0
        count = 1
        n = len(arr)
        
        while i < n:
            level = arr[i:min(i + count, n)]
            level.sort()
            ans.append(level)
            i += count
            count *= 2
            
        return ans