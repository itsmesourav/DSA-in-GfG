class Solution:
    def getMaxWeight(self, s: str) -> int:
        n = len(s)
        next1 = 0  # represents dp[i + 1]
        next2 = 0  # represents dp[i + 2]

        for i in range(n - 1, -1, -1):
            # Choice 1: Take current character as single (contributes 1)
            curr = 1 + next1

            # Choice 2: Pair with the next character (if available)
            if i + 1 < n:
                # If characters are the same, 1 toggle is needed (4 - 1 = 3)
                # If they are already different, no toggle is needed (4)
                pairWeight = 3 if s[i] == s[i + 1] else 4
                curr = max(curr, pairWeight + next2)

            # Shift variables for the next iteration
            next2 = next1
            next1 = curr

        return next1