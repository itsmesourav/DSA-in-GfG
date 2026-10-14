
class Solution:
    def findRollOut(self, s, roll):
        n = len(s)
        shifts = [0] * (n + 1)

        for x in roll:
            shifts[x] += 1

        for i in range(n - 1, 0, -1):
            shifts[i] += shifts[i + 1]

        result = []

        for i in range(n):
            new_char = (ord(s[i]) - ord('a') + shifts[i + 1]) % 26
            result.append(chr(new_char + ord('a')))

        return ''.join(result)
