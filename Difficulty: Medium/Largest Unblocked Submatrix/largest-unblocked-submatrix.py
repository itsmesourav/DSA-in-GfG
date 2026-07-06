class Solution:
    def largestArea(self, n, m, k, arr):
        if k == 0:
            return n * m

        rows = sorted(r for r, c in arr)
        cols = sorted(c for r, c in arr)

        def max_gap(size, blocked):
            best = blocked[0] - 1          # before first blocked
            for i in range(1, len(blocked)):
                best = max(best, blocked[i] - blocked[i - 1] - 1)
            best = max(best, size - blocked[-1])   # after last blocked
            return best

        max_rows = max_gap(n, rows)
        max_cols = max_gap(m, cols)

        return max_rows * max_cols