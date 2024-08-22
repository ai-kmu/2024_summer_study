from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        max_prob = {start_node: 1.0}
        q = [(-1.0, start_node)]

        while q:
            cur_prob, cur_v = heappop(q)

            if cur_v == end_node:
                return -cur_prob

            for next_v, path_prob in graph[cur_v]:
                next_prob = -cur_prob * path_prob
                if next_prob > max_prob.get(next_v, 0):
                    max_prob[next_v] = next_prob
                    heappush(q, (-next_prob, next_v))

        return 0.0
