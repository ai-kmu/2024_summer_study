class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        parent = list(range(len(s)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        # 각 쌍에 대해 Union 연산을 수행하여 연결된 그룹을 찾음
        for a, b in pairs:
            union(a, b)

        # 같은 루트에 있는 인덱스들을 그룹화
        from collections import defaultdict
        groups = defaultdict(list)
        for i in range(len(s)):
            groups[find(i)].append(i)

        # 각 그룹별로 문자를 정렬하여 사전순으로 배치
        res = list(s)
        for indices in groups.values():
            sorted_chars = sorted(res[i] for i in indices)
            for i, char in zip(sorted(indices), sorted_chars):
                res[i] = char

        return ''.join(res)
