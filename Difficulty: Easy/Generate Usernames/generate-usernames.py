class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:
        used = set(arr)
        cnt = {}
        res = []
        
        for s in arr:
            if s not in cnt:
                cnt[s] = 1
                res.append(s)
                
            else:
                i = cnt[s]
                
                while s + str(i) in used:
                    i += 1
                    
                name = s + str(i)
                used.add(name)
                cnt[s] = i + 1
                res.append(name)
            
        return res