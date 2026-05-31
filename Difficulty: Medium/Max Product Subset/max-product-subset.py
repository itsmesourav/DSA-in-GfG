class Solution:
    def findMaxProduct(self, arr):
        n = len(arr)

        if n == 1:
            return arr[0]

        prod = 1
        neg_count = 0
        zero_count = 0
        max_neg = -11  # negative closest to zero

        for x in arr:
            if x == 0:
                zero_count += 1
                continue

            prod *= x

            if x < 0:
                neg_count += 1
                max_neg = max(max_neg, x)

        # All zeros
        if zero_count == n:
            return 0

        # One negative and rest zeros
        if neg_count == 1 and zero_count + neg_count == n:
            return 0

        # Odd number of negatives: remove the negative
        # having minimum absolute value
        if neg_count % 2:
            prod //= max_neg

        return prod % (10**9 + 7)