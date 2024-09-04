class Solution(object):
    def maxSubArray(self, nums):
        
        DP = [0] * len(nums)
        DP[0] = nums[0]

        for i in range(1, len(nums)):
            DP[i] = max(DP[i-1] + nums[i], nums[i])
        
        return max(DP)
