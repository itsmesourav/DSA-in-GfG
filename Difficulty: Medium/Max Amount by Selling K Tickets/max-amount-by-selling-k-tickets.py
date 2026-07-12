import heapq

class Solution:
    def maxAmount(self, arr, k):
        MOD = 10**9 + 7

        # Python has a min-heap, so store negative values.
        heap = [-x for x in arr]
        heapq.heapify(heap)

        ans = 0

        while k > 0 and heap:
            x = -heapq.heappop(heap)
            ans = (ans + x) % MOD
            k -= 1

            if x > 1:
                heapq.heappush(heap, -(x - 1))

        return ans