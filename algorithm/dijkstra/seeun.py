class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g = collections.defaultdict(dict)

        for i, (u, v) in enumerate(edges):
            g[u][v] = succProb[i]
            g[v][u] = succProb[i]
        visited = set()
        q = [(-1, start)]

        while q:
            p, node = heapq.heappop(q)
            if node in visited:
                continue
            if node == end:
                return -p
            visited.add(node)
            for i in g[node]:
                heapq.heappush(q, (p*g[node][i], i))

        return 0
