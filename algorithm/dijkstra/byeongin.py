import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        dist = [0.0 for _ in range(n)] 
        dist[start_node] = 1.0 
        graph = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        queue = [(-1.0, start_node)]
        while queue:
            cur_dist, cur_node = heapq.heappop(queue)
            cur_dist *= -1
            if(dist[cur_node] > cur_dist):
                continue
            for new_node, new_dist in graph[cur_node]:
                tmp_dist = cur_dist * new_dist
                if(tmp_dist > dist[new_node]):
                    dist[new_node] = tmp_dist
                    heapq.heappush(queue, [-tmp_dist, new_node])

        return dist[end_node]
