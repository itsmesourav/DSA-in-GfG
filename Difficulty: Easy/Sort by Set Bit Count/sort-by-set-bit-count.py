class Solution:
    def sortBySetBitCount(self, arr):
        return sorted(arr, key=lambda x: -x.bit_count())