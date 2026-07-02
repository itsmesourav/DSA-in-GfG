class Solution:
    def divisibleByK(self, arr, k):
        dp = [False] * k

        for num in arr:
            rem = num % k
            new_dp = dp[:]

            # Start a new subset with current element
            new_dp[rem] = True

            # Add current element to all existing subsets
            for r in range(k):
                if dp[r]:
                    new_dp[(r + rem) % k] = True

            dp = new_dp

            # If remainder 0 is achievable, we're done
            if dp[0]:
                return True

        return False