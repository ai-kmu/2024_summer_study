class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.s = s
        N = len(s)
        self.adj = [[] for _ in range(N)]

        for i, j in pairs:
            self.adj[i].append(j)
            self.adj[j].append(i)
            
        self.visited = [0] * N
        ans = [''] * N
        
        for i in range(N):
            if not self.visited[i]:
                nei = []
                self.dfs(i, nei)
            
                if not nei:
                    ans[i] = s[i]
                else:
                    a = sorted(nei, key=lambda x: x[1])
                    b = sorted(nei, key=lambda x: x[0])
                    
                    for i in range(len(nei)):
                        ans[b[i][0]] = a[i][1]
            
        return ''.join(ans)

    def dfs(self, i, nei):
        nei.append((i, self.s[i]))
        self.visited[i] = 1
        for j in self.adj[i]:
            if not self.visited[j]:
                self.dfs(j, nei)
