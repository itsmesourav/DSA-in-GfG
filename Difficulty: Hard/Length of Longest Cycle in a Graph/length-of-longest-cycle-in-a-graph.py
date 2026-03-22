class Solution:
    def longestCycle(self, V, edges):
        visited = [0] * V
        depth = [0] * V
        ans = -1
        
        graph = [-1] * V
        for u, v in edges:
            graph[u] = v
        
        def dfs(node, d):
            nonlocal ans
            visited[node] = 1
            depth[node] = d
            
            v = graph[node]
            if v != -1:
                
                if visited[v] == 0:
                    dfs(v, d + 1)
                elif visited[v] == 1:
                    ans = max(ans, d - depth[v] + 1)
                        
            visited[node] = 2
        
        for i in range(V):
            if visited[i] == 0:
                dfs(i ,0)
        
        return ans