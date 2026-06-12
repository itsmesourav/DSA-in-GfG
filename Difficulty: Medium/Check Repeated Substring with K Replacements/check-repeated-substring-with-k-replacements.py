class Solution:
    def kSubstr(self, s: str, k: int) -> bool:
        n = len(s)
        
        if n % k != 0:
            return False
            
        
        blocks = [s[i:i + k] for i in range(0, n, k)]
        m = len(blocks)
        
        freq = {}
        mx = 0

        for b in blocks:
            freq[b] = freq.get(b, 0) + 1
            mx = max(mx, freq[b])

        # Possible iff all but at most one block are already identical
        return mx >= m - 1
