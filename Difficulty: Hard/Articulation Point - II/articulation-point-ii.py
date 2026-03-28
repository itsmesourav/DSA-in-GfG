class Solution:
    def articulationPoints(self, V, edges):
        from collections import defaultdict
        
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * V
        tin = [-1] * V
        low = [-1] * V
        mark = [0] * V
        
        timer = 0  # ✅ FIX
        
        def dfs(node, parent):
            nonlocal timer
            visited[node] = True
            tin[node] = low[node] = timer
            timer += 1
            child = 0
            
            for nei in adj[node]:
                if nei == parent:
                    continue
                
                if not visited[nei]:
                    dfs(nei, node)
                    low[node] = min(low[node], low[nei])
                    
                    if low[nei] >= tin[node] and parent != -1:
                        mark[node] = 1
                        
                    child += 1
                else:
                    low[node] = min(low[node], tin[nei])
                    
            if parent == -1 and child > 1:
                mark[node] = 1
        
        for i in range(V):
            if not visited[i]:
                dfs(i, -1)
        
        ans = [i for i in range(V) if mark[i] == 1]
        return ans if ans else [-1]