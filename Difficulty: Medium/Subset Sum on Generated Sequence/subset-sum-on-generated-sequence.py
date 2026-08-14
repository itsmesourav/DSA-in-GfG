class Solution:
    def isPossible(self, arr, s, x):
        if x == 0:
            return True
            
        if s > x:
            return False
            
        seq = [s]
        current_sum = s
        
        for a in arr:
            next_val = current_sum + a
            
            if next_val > x:
                break
        
            seq.append(next_val)
            current_sum += next_val
            
        for val in reversed(seq):
            if x >= val:
                x -= val
                
        return x == 0