class Solution(object):
    def permute(self, nums):
        def dfs(depth):
            if depth == len(nums):
                results.append(result[:])
            else:
                for i in range(len(nums)):
                    if not visited[i]:
                        visited[i] = True
                        result[depth] = nums[i]
                        dfs(depth+1)
                        visited[i] = False

        visited = [False] * len(nums)
        result = [0] * len(nums)
        results = []

        dfs(0)

        return results
