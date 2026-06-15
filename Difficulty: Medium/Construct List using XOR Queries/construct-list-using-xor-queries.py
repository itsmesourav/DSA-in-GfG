class Solution:
    def constructList(self, queries):
        arr = [0]      # store values in transformed form
        xr = 0         # cumulative XOR
        
        for t, x in queries:
            if t == 0:
                arr.append(x ^ xr)
            else:
                xr ^= x
        
        ans = [num ^ xr for num in arr]
        ans.sort()
        return ans