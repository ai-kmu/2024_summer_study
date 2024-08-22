from typing import List
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # 그래프를 인접 리스트로 표현
        graph = {i: {} for i in range(n)}
        for i, (u, v) in enumerate(edges):  # edge : 간선 정보 나타냄
            graph[u][v] = succProb[i]   # succProb : 해당 edge의 성공 확률
            graph[v][u] = succProb[i]

        # 다익스트라 알고리즘을 사용하여 최대 확률 경로를 찾기
        def dijkstra(graph, start):
            probabilities = {node: 0 for node in graph}
            probabilities[start] = 1
            queue = []
            heapq.heappush(queue, (-1, start))  # Max heap을 위해 확률에 음수를 사용

            while queue:
                current_prob, current_node = heapq.heappop(queue)
                current_prob = -current_prob  # 다시 양수로 변환

                if current_node == end_node:
                    return current_prob
                
                for neighbor, edge_prob in graph[current_node].items():
                    new_prob = current_prob * edge_prob
                    if new_prob > probabilities[neighbor]:
                        probabilities[neighbor] = new_prob
                        heapq.heappush(queue, (-new_prob, neighbor))
            
            return 0.0

        # dijkstra를 사용하여 시작 노드에서 끝 노드까지의 최대 확률을 계산
        return dijkstra(graph, start_node)
