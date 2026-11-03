
class Solution:
    def maximumWeight(self, n, edges, queries):
        edges.sort(key=lambda x: x[2])

        arr = sorted([(x, i) for i, x in enumerate(queries)])

        par = list(range(n + 1))
        sz = [1] * (n + 1)

        def find(x):
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x

        ans = [0] * len(queries)
        total = 0
        j = 0

        for x, idx in arr:
            while j < len(edges) and edges[j][2] <= x:
                u, v, w = edges[j]

                a = find(u)
                b = find(v)

                if a != b:
                    total += sz[a] * sz[b]

                    if sz[a] < sz[b]:
                        a, b = b, a

                    par[b] = a
                    sz[a] += sz[b]

                j += 1

            ans[idx] = total

        return ans
