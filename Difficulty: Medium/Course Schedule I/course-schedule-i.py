from collections import defaultdict, deque
class Solution:
    def canFinish(self, n, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * n
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
            
        queue = deque()
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        completed = 0
        
        while queue:
            course = queue.popleft()
            completed += 1
            
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return completed == n
        
