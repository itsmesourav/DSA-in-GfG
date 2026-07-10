class Solution:
    def longestPath(self, mat, xs, ys, xd, yd):
        n = len(mat)
        m = len(mat[0])

        if mat[xs][ys] == 0 or mat[xd][yd] == 0:
            return -1

        def dfs(x, y):
            if x == xd and y == yd:
                return 0

            mat[x][y] = 0      # mark visited
            ans = -1

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 1:
                    res = dfs(nx, ny)
                    if res != -1:
                        ans = max(ans, res + 1)

            mat[x][y] = 1      # backtrack
            return ans

        return dfs(xs, ys)