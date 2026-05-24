class Solution:
    def checkElements(self, start, end, arr):
        s = set(arr)
        
        for i in range(start, end + 1):
            if i not in s:
                return False
                
        return True
