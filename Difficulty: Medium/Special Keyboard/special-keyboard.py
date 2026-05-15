class Solution:

    def optimalKeys(self, n: int) -> int:
        # For small n, pressing 'A' every time is optimal
        if n <= 6:
            return n
        
        # dp[i] = maximum A's possible with i key presses
        dp = [0] * (n + 1)
        
        for i in range(1, 7):
            dp[i] = i
        
        # Try every possible breakpoint
        for i in range(7, n + 1):
            dp[i] = 0
            
            # j = point where we start Ctrl+A, Ctrl+C and then paste
            for j in range(i - 3, 0, -1):
                # Remaining operations after copy sequence
                pastes = i - j - 2
                
                # Total = current content * (number of pastes + 1)
                dp[i] = max(dp[i], dp[j] * (pastes + 1))
        
        return dp[n]