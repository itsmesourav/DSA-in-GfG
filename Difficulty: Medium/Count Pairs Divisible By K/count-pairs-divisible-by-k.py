class Solution:
    def countKdivPairs(self, arr, k):
        freq = {}
        count = 0

        for num in arr:
            rem = num % k
            need = (k - rem) % k

            count += freq.get(need, 0)
            freq[rem] = freq.get(rem, 0) + 1

        return count