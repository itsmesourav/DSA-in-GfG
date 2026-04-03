class Solution:
    def graycode(self, n):
        result = []
        
        for i in range(1 << n):  # 2^n numbers
            gray = i ^ (i >> 1)
            # convert to binary and pad with leading zeros
            result.append(format(gray, f'0{n}b'))
        
        return result