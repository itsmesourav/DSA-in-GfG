import heapq

class Solution:
    def countPaths(self, V, edges):
        MOD = 10**9 + 7
        
        # Build graph
        graph = [[] for _ in range(V)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Min heap (distance, node)
        pq = [(0, 0)]
        
        dist = [float('inf')] * V
        ways = [0] * V
        
        dist[0] = 0
        ways[0] = 1
        
        while pq:
            d, node = heapq.heappop(pq)
            
            # Skip outdated entries
            if d != dist[node]:
                continue
            
            for nei, wt in graph[node]:
                new_dist = d + wt
                
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    ways[nei] = ways[node]
                    heapq.heappush(pq, (new_dist, nei))
                
                elif new_dist == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD
        
        return ways[V - 1] % MOD