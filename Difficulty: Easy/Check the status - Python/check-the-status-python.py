class Solution:
    def checkStatus(self, a, b, flag):
        condition1 = ((a >= 0) ^ (b >= 0)) and (not flag)
        
        condition2 = (a < 0 and b < 0) and flag
        
        return condition1 or condition2