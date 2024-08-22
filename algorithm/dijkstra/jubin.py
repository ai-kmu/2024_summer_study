class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):

        # 그래프 초기화
        graph = {i: {} for i in range(n)}

        # 그래프 생성
        for i, (u, v) in enumerate(edges):
            prob = succProb[i]
            graph[u][v] = prob
            graph[v][u] = prob

        max_heap = [(-1, start_node)]  # (확률, 노드), 확률을 음수로 저장하여 최대 힙처럼 사용
        probs = [0] * n
        probs[start_node] = 1

        while max_heap:
            
            # 현재 확률이 가장 큰 노드를 꺼냄
            curr_prob, node = heapq.heappop(max_heap)
            curr_prob = -curr_prob  # 원래 확률로 되돌림

            # 이미 더 높은 확률로 방문한 적이 있다면 스킵
            if curr_prob < probs[node]:
                continue

            # 인접 노드들의 확률 갱신
            for neighbor, edge_prob in graph[node].items():
                new_prob = curr_prob * edge_prob
                if new_prob > probs[neighbor]:
                    probs[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))  # 최대 힙 유지

        return probs[end_node]
