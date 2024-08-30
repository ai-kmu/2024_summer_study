class Solution(object):

    # 부모 노드를 찾는 함수
    def getParent(self, parent, x):
        if parent[x] == x:
            return x
        return parent[x] = self.getParent(parent, parent[x])

    # 두 부모 노드를 합침
    def unionParent(self, parent, rank, a, b):
        a = self.getParent(parent, a)
        b = self.getParent(parent, b)

        if a != b:
            if rank[a] > rank[b]:
                parent[b] = a
            elif rank[a] < rank[b]:
                parent[a] = b
            else:
                parent[b] = a
                rank[a] += 1

    def smallestStringWithSwaps(self, s, pairs):
        n = len(s)
        parent = list(range(n))
        rank = [0] * n

        for a, b in pairs:
            self.unionParent(parent, rank, a, b)

        from collections import defaultdict
        groups = defaultdict(list)

        for i in range(n):
            root = self.getParent(parent, i)
            groups[root].append(s[i])

        for group in groups.values():
            group.sort(reverse=True)
        
        result = []
        for i in range(n):
            root = self.getParent(parent, i)
            result.append(groups[root].pop())

        return ''.join(result)
