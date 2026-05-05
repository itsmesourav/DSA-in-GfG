class Solution:
    def sumXOR(self, arr):
        n = len(arr)
        total_sum = 0
        
        # Iterate over each bit position
        for bit in range(32):  # enough for integers up to 1e9
            count1 = 0
            
            # Count elements with current bit set
            for num in arr:
                if num & (1 << bit):
                    count1 += 1
            
            count0 = n - count1
            
            # Contribution of this bit
            total_sum += count1 * count0 * (1 << bit)
        
        return total_sum