class Solution:
    
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a < b:
            self.parent[b] = a
        else:
            self.parent[a] = b

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.parent = list(range(len(s))) # 빈 parent list 생성
        for a, b in pairs:
            self.union(a, b)

        groups = defaultdict(list)
        for i, c in enumerate(s):
            parent = self.find(i)
            groups[parent].append(c)

        for i in groups:
            groups[i].sort(reverse=True)

        res = []
        for i in range(len(s)):
            res.append(groups[self.find(i)].pop())
        
        return ''.join(res)
