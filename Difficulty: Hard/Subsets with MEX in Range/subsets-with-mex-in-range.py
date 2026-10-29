from typing import List

class Solution:
    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:
        MOD = 10**9 + 7

        # Determine the maximum value limit to handle bounds properly
        max_val = max(arr) if arr else 0
        max_limit = max(max_val + 2, r + 2)

        # Count frequencies of each element
        count = [0] * (max_limit + 1)
        for x in arr:
            if x <= max_limit:
                count[x] += 1

        # Suffix sums of counts: total elements strictly greater than x
        suffix_sum = [0] * (max_limit + 2)
        for i in range(max_limit, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + count[i]

        # Prefix products of (2^{c_v} - 1) mod MOD
        pref_prod = [1] * (max_limit + 2)
        current_prod = 1
        for v in range(max_limit + 1):
            pref_prod[v] = current_prod
            ways_v = (pow(2, count[v], MOD) - 1) % MOD
            current_prod = (current_prod * ways_v) % MOD
        pref_prod[max_limit + 1] = current_prod

        total_ans = 0
        for x in range(l, r + 1):
            # Product for values < x
            p1 = pref_prod[x]

            # Product for values > x (2^(sum of counts > x))
            p2 = pow(2, suffix_sum[x + 1], MOD)

            ways = (p1 * p2) % MOD
            total_ans = (total_ans + ways) % MOD

        return total_ans