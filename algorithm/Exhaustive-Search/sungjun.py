class Solution:
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        tmp = []
        result = []
        depth = len(nums)
        visited = [False] * 10

        def recur(num):
            if(num == depth):
                result.append(tmp[:])
                return
            
            for i in range(depth):
                if visited[i]: continue
                visited[i] = True
                tmp.append(nums[i])
                recur(num + 1)
                tmp.pop()
                visited[i] = False
        
        recur(0)

        return result
