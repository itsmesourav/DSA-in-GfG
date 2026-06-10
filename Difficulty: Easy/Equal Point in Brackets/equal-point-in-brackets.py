class Solution:
    def findIndex(self, s):
        n = len(s)
        
        left_open = 0
        right_close = s.count(')')
        
        for k in range(n + 1):
            if left_open == right_close:
                return k
                
            if k < n:
                if s[k] == '(':
                    left_open += 1
                else:
                    right_close -= 1
