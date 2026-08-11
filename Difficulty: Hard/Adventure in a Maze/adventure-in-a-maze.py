class Solution:

    def findWays(self, grid):
        MOD = 10**9 + 7
        n = len(grid)

        ways = [[0] * n for _ in range(n)]

        # -1 means the cell is unreachable
        best = [[-1] * n for _ in range(n)]

        ways[0][0] = 1
        best[0][0] = grid[0][0]

        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                # Come from the left.
                # The left cell must allow moving Right.
                if j > 0 and grid[i][j - 1] in (1, 3):
                    if best[i][j - 1] != -1:
                        ways[i][j] = (
                            ways[i][j] + ways[i][j - 1]
                        ) % MOD

                        best[i][j] = max(
                            best[i][j],
                            best[i][j - 1] + grid[i][j]
                        )

                # Come from above.
                # The upper cell must allow moving Down.
                if i > 0 and grid[i - 1][j] in (2, 3):
                    if best[i - 1][j] != -1:
                        ways[i][j] = (
                            ways[i][j] + ways[i - 1][j]
                        ) % MOD

                        best[i][j] = max(
                            best[i][j],
                            best[i - 1][j] + grid[i][j]
                        )

        # Destination unreachable
        if best[n - 1][n - 1] == -1:
            return [0, 0]

        return [ways[n - 1][n - 1], best[n - 1][n - 1]]