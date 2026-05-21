class Solution:
    def cntOnes(self, grid):
        n = len(grid)
        m = len(grid[0])

        visited = [[False] * m for _ in range(n)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # DFS to mark all boundary-connected 1s
        def dfs(r, c):
            visited[r][c] = True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < n and 0 <= nc < m and
                    grid[nr][nc] == 1 and not visited[nr][nc]):
                    dfs(nr, nc)

        # Traverse boundary cells
        for i in range(n):
            if grid[i][0] == 1 and not visited[i][0]:
                dfs(i, 0)

            if grid[i][m - 1] == 1 and not visited[i][m - 1]:
                dfs(i, m - 1)

        for j in range(m):
            if grid[0][j] == 1 and not visited[0][j]:
                dfs(0, j)

            if grid[n - 1][j] == 1 and not visited[n - 1][j]:
                dfs(n - 1, j)

        # Count enclosed 1s
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    count += 1

        return count