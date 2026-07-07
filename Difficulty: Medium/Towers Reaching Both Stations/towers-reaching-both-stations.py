from collections import deque

class Solution:
    def countCoordinates(self, mat):
        n = len(mat)
        m = len(mat[0])

        def bfs(starts):
            vis = [[False] * m for _ in range(n)]
            q = deque()

            for r, c in starts:
                if not vis[r][c]:
                    vis[r][c] = True
                    q.append((r, c))

            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                x, y = q.popleft()

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < n and 0 <= ny < m and
                        not vis[nx][ny] and
                        mat[nx][ny] >= mat[x][y]):
                        vis[nx][ny] = True
                        q.append((nx, ny))

            return vis

        pacific = [(0, j) for j in range(m)] + [(i, 0) for i in range(n)]
        atlantic = [(n - 1, j) for j in range(m)] + [(i, m - 1) for i in range(n)]

        p_vis = bfs(pacific)
        q_vis = bfs(atlantic)

        ans = 0
        for i in range(n):
            for j in range(m):
                if p_vis[i][j] and q_vis[i][j]:
                    ans += 1

        return ans