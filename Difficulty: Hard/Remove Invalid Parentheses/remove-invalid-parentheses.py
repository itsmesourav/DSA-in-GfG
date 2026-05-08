class Solution:
    def validParenthesis(self, s):
        
        # Function to check if a string is valid
        def isValid(st):
            count = 0
            for ch in st:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    
                if count < 0:
                    return False
                    
            return count == 0
        
        res = []
        visited = set()
        queue = [s]
        found = False
        
        visited.add(s)
        
        while queue:
            curr = queue.pop(0)
            
            # If valid, add to result
            if isValid(curr):
                res.append(curr)
                found = True
            
            # Stop generating next level after finding minimum removals
            if found:
                continue
            
            # Generate all possible strings by removing one parenthesis
            for i in range(len(curr)):
                
                # Skip non-parenthesis characters
                if curr[i] not in ('(', ')'):
                    continue
                
                nxt = curr[:i] + curr[i+1:]
                
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
        
        return sorted(list(set(res)))