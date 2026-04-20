import math

class Solution:
    def pour(self, fromCap, toCap, d):
        fromJug = fromCap
        toJug = 0
        step = 1

        while fromJug != d and toJug != d:
            # Transfer water
            temp = min(fromJug, toCap - toJug)
            toJug += temp
            fromJug -= temp
            step += 1

            if fromJug == d or toJug == d:
                break

            # If fromJug becomes empty, fill it
            if fromJug == 0:
                fromJug = fromCap
                step += 1

            # If toJug becomes full, empty it
            if toJug == toCap:
                toJug = 0
                step += 1

        return step

    def minSteps(self, m, n, d):
        # If not possible
        if d > max(m, n):
            return -1
        
        if d % math.gcd(m, n) != 0:
            return -1
        
        # Try both ways
        return min(self.pour(m, n, d), self.pour(n, m, d))