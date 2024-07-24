class Solution(object):
    def permute(self, nums):
        result = []

        def permute(p, used):
            if len(p) == len(nums):
                result.append(p[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    p.append(nums[i])
                    permute(p, used) # 재귀함수
                    p.pop()
                    used[i] = False
        
        permute([], [False] * len(nums))

        return result
