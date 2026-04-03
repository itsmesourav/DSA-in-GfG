class Solution:
    def diagView(self, mat):
        n = len(mat)
        ans = []
        
        for s in range(2 * n - 1):
            row = 0 if s < n else s - n + 1
            col = s if s < n else n - 1
            
            while row < n and col >= 0:
                ans.append(mat[row][col])
                row += 1
                col -= 1
        
        return ans