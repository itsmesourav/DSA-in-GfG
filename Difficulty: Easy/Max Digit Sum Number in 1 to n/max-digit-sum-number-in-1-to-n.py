class Solution:
    def findMax(self, n):
        s = str(n)
        best = n
        best_sum = sum(map(int, s))

        for i in range(len(s)):
            if s[i] != '0':
                candidate = int(
                    s[:i] + str(int(s[i]) - 1) + '9' * (len(s) - i - 1)
                )

                digit_sum = sum(map(int, str(candidate)))

                if digit_sum > best_sum or (digit_sum == best_sum and candidate > best):
                    best = candidate
                    best_sum = digit_sum

        return best