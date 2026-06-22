class Solution:
    def maxPeopleDefeated(self, p):
        def sumSquares(n):
            return n * (n + 1) * (2 * n + 1) // 6

        low, high = 0, 100000  # sufficiently large upper bound

        while low <= high:
            mid = (low + high) // 2

            if sumSquares(mid) <= p:
                low = mid + 1
            else:
                high = mid - 1

        return high