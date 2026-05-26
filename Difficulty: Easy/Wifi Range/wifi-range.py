class Solution:
    def wifiRange(self, s, x):
        n = len(s)

        # Difference array
        cover = [0] * (n + 1)

        for i in range(n):
            if s[i] == '1':
                left = max(0, i - x)
                right = min(n - 1, i + x)

                cover[left] += 1
                if right + 1 < n:
                    cover[right + 1] -= 1

        # Prefix sum to check coverage
        curr = 0
        for i in range(n):
            curr += cover[i]
            if curr <= 0:
                return False

        return True