class Solution:
    def transform(self, s1, s2): 
        #code here
        n = len(s1)

        if n != len(s2):
            return -1

        # Same characters are necessary.
        if sorted(s1) != sorted(s2):
            return -1

        # Find the longest suffix of s2 that is a subsequence of s1.
        i = n - 1
        j = n - 1

        while i >= 0 and j >= 0:
            if s1[i] == s2[j]:
                j -= 1
            i -= 1

        # s2[j+1:] is the part that can remain.
        return j + 1