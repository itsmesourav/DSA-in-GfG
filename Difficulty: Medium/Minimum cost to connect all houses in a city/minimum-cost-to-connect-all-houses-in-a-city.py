class Solution:
    def minCost(self, houses):
        n = len(houses)
        
        visited = [False] * n
        minDist = [float('inf')] * n
        
        # Start from house 0
        minDist[0] = 0
        total_cost = 0
        
        for _ in range(n):
            # Pick the minimum distance unvisited node
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or minDist[i] < minDist[u]):
                    u = i
            
            visited[u] = True
            total_cost += minDist[u]
            
            # Update distances
            for v in range(n):
                if not visited[v]:
                    cost = abs(houses[u][0] - houses[v][0]) + abs(houses[u][1] - houses[v][1])
                    if cost < minDist[v]:
                        minDist[v] = cost
        
        return total_cost