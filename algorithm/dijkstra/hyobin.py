class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        probs = [0.0]*n
        graph = defaultdict(list)
      
        for i, (u,v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        probs[start_node] = 1.0
        q = [(-1.0, start_node)]

        while q:
            cur_prob, cur_v = heappop(q)

            if cur_v == end_node:
                return -cur_prob

            for next_v, path_prob in graph[cur_v]:
                if -cur_prob * path_prob > probs[next_v]:
                    probs[next_v] = -cur_prob*path_prob
                    heappush(q, (-probs[next_v], next_v))

        return 0.00000
