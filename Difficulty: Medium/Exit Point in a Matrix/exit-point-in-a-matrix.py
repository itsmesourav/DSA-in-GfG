class Solution:
    def exitPoint(self, mat):
        n = len(mat)
        m = len(mat[0])

        i, j = 0, 0
        direction = 0  # 0=Right, 1=Down, 2=Left, 3=Up

        while True:
            if mat[i][j] == 1:
                direction = (direction + 1) % 4
                mat[i][j] = 0

            # Move according to direction
            if direction == 0:
                j += 1
            elif direction == 1:
                i += 1
            elif direction == 2:
                j -= 1
            else:
                i -= 1

            # Check if exited matrix
            if i < 0:
                return [0, j]
            if i >= n:
                return [n - 1, j]
            if j < 0:
                return [i, 0]
            if j >= m:
                return [i, m - 1]