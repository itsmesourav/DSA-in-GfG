class Solution:
    def determinant(self, mat, n):
        det = 1

        for i in range(n):
            pivot = i

            while pivot < n and mat[pivot][i] == 0:
                pivot += 1

            if pivot == n:
                return 0

            if pivot != i:
                mat[i], mat[pivot] = mat[pivot], mat[i]
                det *= -1

            det *= mat[i][i]

            for j in range(i + 1, n):
                factor = mat[j][i] / mat[i][i]

                for k in range(i, n):
                    mat[j][k] -= factor * mat[i][k]

        return round(det)

    def countSpanTree(self, n, edges):
        # Single node graph
        if n == 1:
            return 1

        # Build Laplacian matrix
        lap = [[0] * n for _ in range(n)]

        for u, v in edges:
            lap[u][u] += 1
            lap[v][v] += 1
            lap[u][v] -= 1
            lap[v][u] -= 1

        # Create cofactor matrix by removing last row & column
        cofactor = []

        for i in range(n - 1):
            row = []
            for j in range(n - 1):
                row.append(lap[i][j])
            cofactor.append(row)

        return self.determinant(cofactor, n - 1)