class Solution:

    def countWithout(self, n: int, d: int) -> int:
        
        if n <= 0:
            return 0

        digits = list(map(int, str(n)))
        m = len(digits)

        # dp(pos, tight, started)
        from functools import lru_cache

        @lru_cache(None)
        def dp(pos, tight, started):
            if pos == m:
                return 1

            limit = digits[pos] if tight else 9
            ans = 0

            for x in range(limit + 1):
                # Leading zeroes don't count as decimal digits.
                if not started and x == 0:
                    ans += dp(pos + 1, tight and x == limit, False)
                elif x == d:
                    continue
                else:
                    ans += dp(pos + 1, tight and x == limit, True)

            return ans

        # Includes 0, so subtract it.
        return dp(0, True, False) - 1