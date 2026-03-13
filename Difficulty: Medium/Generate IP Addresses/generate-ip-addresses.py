class Solution:
    def generateIp(self, s):
        res = []
        
        if len(s) > 12:
            return res
        
        def backtrack(start, parts, path):
            if parts == 4 and start == len(s):
                res.append(path[:-1])
                return
            
            if parts > 4:
                return
            
            for j in range(start, min(start + 3, len(s))):
                if int(s[start: j + 1]) < 256 and  (start == j or s[start] != "0"):
                    backtrack(j + 1, parts +1, path + s[start: j + 1] + ".")
            
        backtrack(0, 0, "")
        return res
            
