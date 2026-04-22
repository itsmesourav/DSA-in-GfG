class Solution:
    def findMean(self, arr, queries):
        n = len(arr)
        
        # Step 1: Build prefix sum array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]
        
        # Step 2: Process queries
        result = []
        for l, r in queries:
            total = prefix[r + 1] - prefix[l]
            length = r - l + 1
            mean = total // length   # floor division
            result.append(mean)
        
        return result