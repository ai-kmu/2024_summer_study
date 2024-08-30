from collections import defaultdict

class Solution:
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])

            return self.parent[x]

        def union(self, x, y):
            rootX = self.find(x)
            rootY = self.find(y)

            if rootX != rootY:
                self.parent[rootY] = rootX

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = self.UnionFind(n)

        for x, y in pairs:
            uf.union(x, y)
        
        groups = defaultdict(list)

        for i in range(n):
            root = uf.find(i)
            groups[root].append(i)

        res = list(s)
        for group in groups.values():
            indices = group
            chars = sorted(res[i] for i in indices)

            for i, char in zip(sorted(indices), chars):
                res[i] = char

        return ''.join(res)
