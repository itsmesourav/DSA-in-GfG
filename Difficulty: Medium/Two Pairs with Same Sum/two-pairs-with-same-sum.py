from collections import defaultdict


class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        n = len(arr)
        by_sum: dict[int, list[tuple[int, int]]] = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                by_sum[arr[i] + arr[j]].append((i, j))

        for a in range(n):
            for b in range(a + 1, n):
                s = arr[a] + arr[b]
                for c, d in by_sum[s]:
                    if (a, b) < (c, d) and a != c and a != d and b != c and b != d:
                        return [a, b, c, d]

        return [-1, -1, -1, -1]