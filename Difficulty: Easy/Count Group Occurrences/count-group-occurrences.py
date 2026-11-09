
class Solution:
    def getCount(self, s, k):
        d = {}

        for i in range(len(s)):
            if i == 0 or s[i] != s[i - 1]:
                d[s[i]] = d.get(s[i], 0) + 1

        return sum(1 for v in d.values() if v == k)
