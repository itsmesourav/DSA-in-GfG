class Solution:
    def findWays(self, matrix, k):
        MOD = 10 ** 9 + 7
        n = len(matrix)
        m = len(matrix[0])

        # Suffix sum of number of 1s
        suf = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                suf[i][j] = (
                    matrix[i][j]
                    + suf[i + 1][j]
                    + suf[i][j + 1]
                    - suf[i + 1][j + 1]
                )

        # firstRow[i][j] = first row below i where suffix count decreases
        firstRow = [[n] * m for _ in range(n)]
        for j in range(m):
            for i in range(n):
                x = i + 1
                while x < n and suf[x][j] == suf[i][j]:
                    x += 1
                firstRow[i][j] = x

        # firstCol[i][j] = first column right of j where suffix count decreases
        firstCol = [[m] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                y = j + 1
                while y < m and suf[i][y] == suf[i][j]:
                    y += 1
                firstCol[i][j] = y

        # Base: one piece
        prev = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if suf[i][j] > 0:
                    prev[i][j] = 1

        for _ in range(2, k + 1):
            # Down cumulative sums
            down = [[0] * m for _ in range(n + 1)]
            for j in range(m):
                for i in range(n - 1, -1, -1):
                    down[i][j] = (prev[i][j] + down[i + 1][j]) % MOD

            # Right cumulative sums
            right = [[0] * (m + 1) for _ in range(n)]
            for i in range(n):
                for j in range(m - 1, -1, -1):
                    right[i][j] = (prev[i][j] + right[i][j + 1]) % MOD

            cur = [[0] * m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    if suf[i][j] == 0:
                        continue
                    ans = 0
                    r = firstRow[i][j]
                    if r < n:
                        ans += down[r][j]
                    c = firstCol[i][j]
                    if c < m:
                        ans += right[i][c]
                    cur[i][j] = ans % MOD
            prev = cur

        return prev[0][0]