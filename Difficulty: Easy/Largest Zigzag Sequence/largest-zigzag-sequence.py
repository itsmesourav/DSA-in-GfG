class Solution:

    def zigzagSequence(self, mat):
        n = len(mat)

        # dp[j] = maximum sum ending at column j
        dp = mat[0][:]

        for i in range(1, n):
            # Find largest and second largest values in dp
            max1 = max(dp)
            idx1 = dp.index(max1)

            max2 = float('-inf')
            for j in range(n):
                if j != idx1:
                    max2 = max(max2, dp[j])

            new_dp = [0] * n

            for j in range(n):
                # Cannot use the same column as previous row
                if j == idx1:
                    new_dp[j] = mat[i][j] + max2
                else:
                    new_dp[j] = mat[i][j] + max1

            dp = new_dp

        return max(dp)