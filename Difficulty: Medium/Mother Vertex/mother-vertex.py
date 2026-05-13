class Solution:
    def findMotherVertex(self, V, edges):
        # Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)

        visited = [False] * V
        candidate = -1

        # DFS function
        def dfs(node):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)

        # Step 1: Find a potential mother vertex
        for i in range(V):
            if not visited[i]:
                dfs(i)
                candidate = i

        # Step 2: Verify the candidate
        visited = [False] * V
        dfs(candidate)

        # If candidate cannot reach all vertices
        if not all(visited):
            return -1

        # Step 3: Find the smallest mother vertex
        # Since multiple mother vertices may exist
        for i in range(candidate + 1):
            visited = [False] * V
            dfs(i)
            if all(visited):
                return i

        return candidate