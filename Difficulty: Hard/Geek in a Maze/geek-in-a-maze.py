from collections import deque

class Solution:
    def numberOfCells(self, r: int, c: int, u: int, d: int, mat: list[list[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        # Starting cell is blocked
        if mat[r][c] == '#':
            return 0

        INF = 10**18

        # dist[i][j] = minimum number of downward moves
        # needed to reach (i, j).
        dist = [[INF] * m for _ in range(n)]
        dist[r][c] = 0

        dq = deque([(r, c)])

        while dq:
            x, y = dq.popleft()
            cur = dist[x][y]

            # Left
            if y > 0 and mat[x][y - 1] != '#' and cur < dist[x][y - 1]:
                dist[x][y - 1] = cur
                dq.appendleft((x, y - 1))

            # Right
            if y + 1 < m and mat[x][y + 1] != '#' and cur < dist[x][y + 1]:
                dist[x][y + 1] = cur
                dq.appendleft((x, y + 1))

            # Up: costs 0 downward moves
            if x > 0 and mat[x - 1][y] != '#' and cur < dist[x - 1][y]:
                dist[x - 1][y] = cur
                dq.appendleft((x - 1, y))

            # Down: costs 1 downward move
            if x + 1 < n and mat[x + 1][y] != '#' and cur + 1 < dist[x + 1][y]:
                dist[x + 1][y] = cur + 1
                dq.append((x + 1, y))

        ans = 0

        for i in range(n):
            for j in range(m):
                if dist[i][j] == INF:
                    continue

                down = dist[i][j]

                # down - up = i - r
                up = down - (i - r)

                if down <= d and up <= u:
                    ans += 1

        return ans