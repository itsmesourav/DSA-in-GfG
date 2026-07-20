class Solution:
    def maxIndexDifference(self, s):
        n = len(s)
        best = [-1] * 26   # best[ch] = farthest reachable end from any processed index of character ch
        ans = -1
        has_a = False

        for i in range(n - 1, -1, -1):
            ch = ord(s[i]) - ord('a')

            if ch == 25:          # 'z'
                far = i
            else:
                if best[ch + 1] == -1:
                    far = i        # no next character exists to the right
                else:
                    far = best[ch + 1]

            best[ch] = max(best[ch], far)

            if ch == 0:           # starting from 'a'
                has_a = True
                ans = max(ans, far - i)

        return ans if has_a else -1