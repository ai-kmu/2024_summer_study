class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        a = [None] * len(nums)
        a[0] = nums[0]

        for i in range(1, len(nums)):
            a[i] = nums[i] + (a[i - 1] if a[i - 1] > 0 else 0)

        return max(a)  
