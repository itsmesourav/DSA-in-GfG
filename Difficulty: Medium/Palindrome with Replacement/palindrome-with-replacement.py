class Solution:
    def minimumSum(self, s: str) -> int:
        n = len(s)
        s = list(s)

        # Check whether a palindrome is possible
        for i in range(n // 2):
            j = n - 1 - i

            if s[i] != '?' and s[j] != '?' and s[i] != s[j]:
                return -1

            if s[i] == '?':
                s[i] = s[j]
            elif s[j] == '?':
                s[j] = s[i]

        # Fill the remaining '?' characters optimally
        i = 0
        while i < n:
            if s[i] != '?':
                i += 1
                continue

            j = i
            while j < n and s[j] == '?':
                j += 1

            left = ord(s[i - 1]) if i > 0 else None
            right = ord(s[j]) if j < n else None

            if left is None and right is None:
                ch = 'a'
            elif left is None:
                ch = chr(right)
            elif right is None:
                ch = chr(left)
            else:
                ch = chr((left + right) // 2)

            for k in range(i, j):
                s[k] = ch

            i = j

        return sum(abs(ord(s[i]) - ord(s[i - 1])) for i in range(1, n)) 