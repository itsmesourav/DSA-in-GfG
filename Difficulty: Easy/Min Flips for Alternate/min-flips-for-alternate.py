
class Solution:
    def minFlips(self, s):
        count1 = 0
        count2 = 0

        for i in range(len(s)):
            # Pattern 1: 010101...
            if s[i] != str(i % 2):
                count1 += 1

            # Pattern 2: 101010...
            if s[i] != str(1 - (i % 2)):
                count2 += 1

        return min(count1, count2)
