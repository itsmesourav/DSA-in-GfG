class Solution:
    def canFormPalindrome(self, s):
        odd_chars = set()
        
        for ch in s:
            if ch in odd_chars:
                odd_chars.remove(ch)
            else:
                odd_chars.add(ch)
        return len(odd_chars) <= 1