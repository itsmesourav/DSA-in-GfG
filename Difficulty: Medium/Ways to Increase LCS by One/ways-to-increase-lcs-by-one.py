class Solution:
    def waysToIncreaseLCSBy1(self, s1, s2):
        n1, n2 = len(s1), len(s2)

        # Prefix LCS DP
        pre = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    pre[i][j] = pre[i - 1][j - 1] + 1
                else:
                    pre[i][j] = max(pre[i - 1][j], pre[i][j - 1])

        lcs = pre[n1][n2]

        # Suffix LCS DP
        suf = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                if s1[i] == s2[j]:
                    suf[i][j] = 1 + suf[i + 1][j + 1]
                else:
                    suf[i][j] = max(suf[i + 1][j], suf[i][j + 1])

        ans = 0

        # Try every insertion position
        for pos in range(n1 + 1):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                ok = False
                for j in range(n2):
                    if s2[j] == ch and pre[pos][j] + 1 + suf[pos][j + 1] == lcs + 1:
                        ok = True
                        break
                if ok:
                    ans += 1

        return ans