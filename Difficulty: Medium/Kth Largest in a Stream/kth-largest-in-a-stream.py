import heapq

class Solution:
    def kthLargest(self, arr, k):
        min_heap = []
        result = []

        for num in arr:
            heapq.heappush(min_heap, num)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

            if len(min_heap) < k:
                result.append(-1)
            else:
                result.append(min_heap[0])

        return result