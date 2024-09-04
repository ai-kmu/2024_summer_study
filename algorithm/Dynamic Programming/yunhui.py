class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = nums[0] 
        curr = nums[0]
        
        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            answer = max(answer, curr)

        return answer 
