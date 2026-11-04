
class Solution:
    def getMinimumDays(self, s: str, p: list[int]) -> int:
        n = len(s)

        def check(day):
            gone = [False] * n

            for i in range(day):
                gone[p[i]] = True

            for i in range(n - 1):
                if not gone[i] and not gone[i + 1]:
                    if s[i] == s[i + 1]:
                        return False

            return True

        l, r = 0, n

        while l < r:
            mid = (l + r) // 2

            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l
