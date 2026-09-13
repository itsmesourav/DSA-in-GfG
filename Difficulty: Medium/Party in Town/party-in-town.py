from collections import deque

class Solution:
    def partyHouse(self, adj: list[list[int]]) -> int:
        n = len(adj)

        def bfs(start):
            dist = [-1] * n
            q = deque()

            dist[start] = 0
            q.append(start)

            farthest = start

            while q:
                node = q.popleft()

                if dist[node] > dist[farthest]:
                    farthest = node

                for nei in adj[node]:
                    nei -= 1  # houses are 1-based

                    if dist[nei] == -1:
                        dist[nei] = dist[node] + 1
                        q.append(nei)

            return farthest, dist[farthest]

        # First BFS: find one endpoint of diameter
        a, _ = bfs(0)

        # Second BFS: find diameter
        b, diameter = bfs(a)

        # Radius = ceil(diameter / 2)
        return (diameter + 1) // 2