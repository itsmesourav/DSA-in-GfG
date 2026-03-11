class Solution:
    def sumSubMins(self, arr):
        stack = []
        res = 0
        MOD = 10**9 + 7
        arr = [0] + arr + [0]
        a = len(arr)
        
        for i in range(a):
            while stack and arr[stack[-1]] > arr[i]:
                mid = stack.pop()
                left = mid - stack[-1]
                right = i - mid
                res += arr[mid] * left * right
            stack.append(i)
        return res % MOD
        
