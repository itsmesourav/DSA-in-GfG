class Solution:
    def reducePairs(self, arr):
        stack = []
        
        for x in arr:
            while stack and (stack[-1] * x < 0):
                if abs(stack[-1]) > abs(x):
                    # current element is destroyed
                    break
                elif abs(stack[-1]) < abs(x):
                    # stack top is destroyed
                    stack.pop()
                    continue
                else:
                    # equal → both destroyed
                    stack.pop()
                    break
            else:
                # no conflict or survived all conflicts
                stack.append(x)
        
        return stack