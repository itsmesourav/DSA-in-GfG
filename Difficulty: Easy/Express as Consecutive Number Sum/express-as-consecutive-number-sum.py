class Solution:
    def isSumOfConsecutive(self, n: int) -> bool:
        return n > 1 and (n & (n - 1)) != 0
        