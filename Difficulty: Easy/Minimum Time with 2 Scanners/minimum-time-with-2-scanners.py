
class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:
        x = (n * s2) // (s1 + s2)

        a = max(x * s1, (n - x) * s2)
        b = max((x + 1) * s1, (n - x - 1) * s2)

        return min(a, b)