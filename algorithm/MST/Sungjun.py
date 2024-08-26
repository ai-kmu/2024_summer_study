class Solution:

    def find(self, x):
        if self.p[x] == x : return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if(x == y) : return 0
        if(self.p[x] == self.p[y]) : self.p[x] -= 1
        if(self.p[x] > self.p[y]) : self.p[x] = y
        else : self.p[y] = x
        return 1

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.p = [i for i in range(len(s))]
        for(a, b) in pairs:
            self.union(a, b)
        # print(self.p)
        graph = defaultdict(lambda: ([], []))
        # print(self.p)
        for idx, key in enumerate(s):
            p = self.find(self.p[idx])
            print(p)
            graph[p][0].append(idx)
            graph[p][1].append(key)

        ans = [''] * len(s)
        for idx, key in graph.values():
            idx.sort()
            key.sort()
            for i, k in zip(idx, key):
                ans[i] = k
        
        return ''.join(ans)
            
