class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        ans = flip = 0
        
        for i in range(n):
            if i >= k and arr[i-k] == 2:
                flip ^= 1
                
            if arr[i] ^ flip == 0:
                if i + k > n:
                    return -1
                ans += 1
                flip ^= 1
                arr[i] = 2
                
        return ans
        
