class Solution:
    def chooseSwap(self, s):
        n = len(s)

        # first occurrence of each character
        first = [-1] * 26
        for i in range(n):
            idx = ord(s[i]) - ord('a')
            if first[idx] == -1:
                first[idx] = i

        c1 = c2 = None

        for i in range(n):
            cur = ord(s[i]) - ord('a')

            # find the smallest character < s[i]
            # whose first occurrence is after i
            for ch in range(cur):
                if first[ch] > i:
                    c1 = chr(cur + ord('a'))
                    c2 = chr(ch + ord('a'))
                    break

            if c1:
                break

        if not c1:
            return s

        ans = []
        for ch in s:
            if ch == c1:
                ans.append(c2)
            elif ch == c2:
                ans.append(c1)
            else:
                ans.append(ch)

        return ''.join(ans)