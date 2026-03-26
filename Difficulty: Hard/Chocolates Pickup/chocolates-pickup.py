class Solution:
    def maxChocolate(self, grid):
        dp = [[[-1]*m for _ in range(m)] for _ in range(n)]
        
        def solve(i, j1, j2):
            if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
                return float('-inf')
                
            if i == n - 1:
                if j1 == j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1] + grid[i][j2]
            
            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]
            
            maxi = float('-inf')
            
            for d1 in [-1, 0, 1]:
                for d2 in [-1, 0, 1]:
                    if j1 == j2:
                        value = grid[i][j1]
                    else:
                        value = grid[i][j1] + grid[i][j2]
                        
                    value += solve(i + 1, j1 + d1, j2 + d2)
                    maxi = max(maxi, value)
            
            dp[i][j1][j2] = maxi
            return maxi
        return solve(0, 0, m-1)