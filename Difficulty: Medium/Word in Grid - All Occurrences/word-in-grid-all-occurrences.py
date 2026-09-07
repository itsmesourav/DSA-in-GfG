class Solution:
    def searchWord(self, mat, word):
        n = len(mat)
        m = len(mat[0])

        # 8 possible directions
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        ans = []
        k = len(word)

        for r in range(n):
            for c in range(m):
                if mat[r][c] != word[0]:
                    continue

                # Try every direction
                for dr, dc in directions:
                    found = True

                    for i in range(1, k):
                        nr = r + i * dr
                        nc = c + i * dc

                        # Out of bounds or character doesn't match
                        if (nr < 0 or nr >= n or
                            nc < 0 or nc >= m or
                            mat[nr][nc] != word[i]):
                            found = False
                            break

                    if found:
                        ans.append([r, c])
                        break   # Don't add same starting cell again

        return ans