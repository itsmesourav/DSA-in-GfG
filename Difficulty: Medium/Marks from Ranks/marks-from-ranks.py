class Solution:
    def getMarks(self, l, r, rank):
        import bisect

        # cumulative[i] = number of valid marks
        # in intervals 0..i
        cumulative = []
        total = 0

        for i in range(len(l)):
            total += r[i] - l[i] + 1
            cumulative.append(total)

        ans = []

        for k in rank:
            # Find the first interval whose cumulative count >= k
            i = bisect.bisect_left(cumulative, k)

            # Number of marks before interval i
            before = cumulative[i - 1] if i > 0 else 0

            # Position within interval (1-indexed)
            offset = k - before

            ans.append(l[i] + offset - 1)

        return ans