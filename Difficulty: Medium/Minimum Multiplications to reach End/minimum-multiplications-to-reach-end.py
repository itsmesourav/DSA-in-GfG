from collections import deque

class Solution:
    def minSteps(self, arr, start, end):
        
        # Distance array
        dist = [float('inf')] * 1000
        
        # BFS queue -> (current_number, steps)
        q = deque()
        q.append((start, 0))
        
        dist[start] = 0
        
        while q:
            node, steps = q.popleft()
            
            # If reached target
            if node == end:
                return steps
            
            for num in arr:
                new_num = (node * num) % 1000
                
                # Visit only if shorter path found
                if steps + 1 < dist[new_num]:
                    dist[new_num] = steps + 1
                    q.append((new_num, steps + 1))
        
        return -1