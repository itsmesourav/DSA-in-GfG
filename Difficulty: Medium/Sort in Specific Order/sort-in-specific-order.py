class Solution:
    def sortIt(self, arr):
        odd = [x for x in arr if x % 2 != 0]
        even = [x for x in arr if x % 2 == 0]

        odd.sort(reverse=True)
        even.sort()

        arr[:] = odd + even
        return arr