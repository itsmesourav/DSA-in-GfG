class Solution:
    def maxValue(self, n: int) -> int:
        set_bits = [0] * 32
        for i in range(32):
            if (n & (1 << i)) != 0:
                set_bits[31 - i] = 1

        ans = 0
        for i in range(30):
            if set_bits[i] == 1:
                ans += (1 << (31 - i))
                if set_bits[i + 1] == 1:
                    set_bits[i + 2] = 0

        if set_bits[30] == 1:
            ans += 2
        if set_bits[31] == 1:
            ans += 1

        return ans