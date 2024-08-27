class Solution:
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x > y:
            self.parent[x] = y
        else:
            self.parent[y] = x
            
    def find(self, x):
        if x == self.parent[x]:
            return x 
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.parent = [i for i in range(len(s))]
        for [a, b] in pairs:
            self.union(a, b)
        
        temp = defaultdict(lambda : ([], []))
        
        for i, ch in enumerate(s):
            p = self.find(i)
            temp[p][0].append(i)
            temp[p][1].append(ch)
    
        answer = [''] * len(s)
        for idx, ch in temp.values():
            idx.sort()
            ch.sort()
            for j in range(len(idx)):
                answer[idx[j]] = ch[j]
        
        return ''.join(answer)
        
    
