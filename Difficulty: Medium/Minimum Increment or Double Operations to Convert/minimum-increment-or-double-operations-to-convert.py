class Solution:
    def countMinOperations(self, arr):
        inc = 0
        max_bits = 0

        for x in arr:
            inc += x.bit_count()      # Number of 1s in binary
            if x > 0:
                max_bits = max(max_bits, x.bit_length() - 1)

        return inc + max_bits