class Solution:

    def subsequenceSum(self, s):
        MOD = 10**9 + 7
        
        n = len(s)
        
        total = 0
        
        for digit in s:
            total = (total + int(digit) *  pow(2, n - 1, MOD)) % MOD
        
        return total