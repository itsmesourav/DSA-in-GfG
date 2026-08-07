class Solution:
    def minEdgesReq(self, n, edges):
        # Not enough edges to connect all vertices
        if len(edges) < n - 1:
            return -1

        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)

        # Count connected components
        components = 0
        for i in range(n):
            if not visited[i]:
                components += 1
                dfs(i)

        return components - 1