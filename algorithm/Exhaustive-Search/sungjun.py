class Solution:
    
    def __init__(self):
        self.depth = 0
        self.tmp = []
        self.input = []
        self.visited = [False] * 7 
        self.ans = []

    def recur(self, num, index):
        if(num == self.depth):
            self.ans.append(self.tmp[:])
            return

        for i in range(self.depth):
            if self.visited[i] == True:
                continue
            
            self.tmp.append(self.input[i])
            self.visited[i] = True
            self.recur(num + 1, i)
            self.visited[i] = False
            self.tmp.pop()

        
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.result = []
        self.depth = len(nums)
        self.input = nums

        for i in range(self.depth):
            self.tmp = []
            self.tmp.append(self.input[i])
            self.visited[i] = True
            self.recur(1 , i)
            self.visited[i] = False

        print(self.ans)

        return self.ans
