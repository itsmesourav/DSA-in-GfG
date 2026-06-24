class Solution:
    def shortestDist(self, mat):
        n = len(mat)

        if mat[0][0] == 0:
            return [[-1]]

        ans = [[0] * n for _ in range(n)]
        dp = [[-1] * n for _ in range(n)]
        # -1 = unvisited, 0 = cannot reach end, 1 = can reach end

        def dfs(i, j):
            if i >= n or j >= n or mat[i][j] == 0:
                return False

            if i == n - 1 and j == n - 1:
                ans[i][j] = 1
                return True

            if dp[i][j] == 0:
                return False

            ans[i][j] = 1

            for jump in range(1, mat[i][j] + 1):

                # right first
                if j + jump < n and dfs(i, j + jump):
                    dp[i][j] = 1
                    return True

                # down next
                if i + jump < n and dfs(i + jump, j):
                    dp[i][j] = 1
                    return True

            ans[i][j] = 0
            dp[i][j] = 0
            return False

        if dfs(0, 0):
            return ans

        return [[-1]]