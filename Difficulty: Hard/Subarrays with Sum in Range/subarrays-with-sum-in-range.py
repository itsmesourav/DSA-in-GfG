class Solution:
    def countSubarray(self, arr, l, r):
        prefix = [0]
        s = 0
        for x in arr:
            s += x
            prefix.append(s)

        def merge_sort(lo, hi):
            if hi - lo <= 1:
                return 0

            mid = (lo + hi) // 2
            cnt = merge_sort(lo, mid) + merge_sort(mid, hi)

            j = k = mid
            for left in prefix[lo:mid]:
                while k < hi and prefix[k] - left < l:
                    k += 1
                while j < hi and prefix[j] - left <= r:
                    j += 1
                cnt += j - k

            prefix[lo:hi] = sorted(prefix[lo:hi])
            return cnt

        return merge_sort(0, len(prefix))