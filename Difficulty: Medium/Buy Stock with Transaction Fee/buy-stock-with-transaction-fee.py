class Solution:
    def maxProfit(self, arr, k):
        if not arr:
            return 0
        
        hold = -arr[0]   # buying first stock
        cash = 0         # no stock in hand
        
        for price in arr[1:]:
            hold = max(hold, cash - price)
            cash = max(cash, hold + price - k)
        
        return cash