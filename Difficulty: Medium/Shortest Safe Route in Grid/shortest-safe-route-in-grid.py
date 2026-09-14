from collections import deque

class Solution:
    def shortestPath(self, mat: list[list[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        unsafe = [[False] * m for _ in range(n)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Mark landmines and cells adjacent to landmines as unsafe
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    unsafe[i][j] = True

                    for di, dj in directions:
                        ni = i + di
                        nj = j + dj

                        if 0 <= ni < n and 0 <= nj < m:
                            unsafe[ni][nj] = True

        q = deque()
        visited = [[False] * m for _ in range(n)]

        # Start from every safe cell in first column
        for i in range(n):
            if not unsafe[i][0]:
                q.append((i, 0, 1))   # distance starts from 1
                visited[i][0] = True

        while q:
            i, j, dist = q.popleft()

            # Reached last column
            if j == m - 1:
                return dist

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if (0 <= ni < n and
                    0 <= nj < m and
                    not unsafe[ni][nj] and
                    not visited[ni][nj]):

                    visited[ni][nj] = True
                    q.append((ni, nj, dist + 1))

        return -1