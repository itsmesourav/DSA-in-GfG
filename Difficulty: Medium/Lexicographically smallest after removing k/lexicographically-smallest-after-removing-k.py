class Solution:
    def lexicographicallySmallest(self, s, k):
        n = len(s)

        # Check if n is a power of 2
        if n > 0 and (n & (n - 1)) == 0:
            k //= 2
        else:
            k *= 2

        # Impossible or resulting string becomes empty
        if k >= n:
            return -1

        stack = []
        rem = k

        for ch in s:
            while rem > 0 and stack and stack[-1] > ch:
                stack.pop()
                rem -= 1
            stack.append(ch)

        # Remove remaining characters from the end
        while rem > 0:
            stack.pop()
            rem -= 1

        ans = ''.join(stack)

        return ans if ans else -1