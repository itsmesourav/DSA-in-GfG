class Solution:
    def segregate0and1(self, arr):
        count0 = arr.count(0)
        
        for i in range(len(arr)):
            if i < count0:
                arr[i] = 0
            else:
                arr[i] = 1