class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = -0x3f3f3f3f
        dp = [0] * (len(nums) + 1)
        dp[0] = 0

        for i in range(1, len(nums) + 1):
            if(dp[i-1] + nums[i-1] > nums[i-1]):
                dp[i] = dp[i-1] + nums[i-1]
            else:
                dp[i] = nums[i-1]

            sum = max(sum, dp[i])

        print(sum)
        return sum
        
