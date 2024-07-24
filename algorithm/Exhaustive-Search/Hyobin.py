class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        visited = [0] * len(nums)
        answer = []
        tmp = []

        def dfs(tmplist, numlist):
            if len(tmplist) == len(numlist):
                answer.append(tmplist[:])
                return

            for i, val in enumerate(numlist):
                if visited[i] == 1:
                    continue

                tmplist.append(val)
                visited[i] = 1

                dfs(tmplist, numlist)

                tmplist.pop()
                visited[i] = 0

        dfs(tmp, nums)
        
        return answer