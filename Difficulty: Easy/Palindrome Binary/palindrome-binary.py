class Solution:
    def isPallindrome(self, N):
        left = N.bit_length() - 1
        right = 0
        
        while left > right:
            if ((N >> left) & 1) != ((N >> right) & 1):
                return 0
            left -= 1
            right += 1
            
        return 1