class Solution(object):
    def maxSubArray(self, nums, start=None, end=None):
        if start == None: 
            start = 0
        if end == None:
            end = len(nums) - 1
        #베이스케이스
        if start == end:
            return nums[start]
        
        mid = (start + end) // 2
        
        left_max_sum = self.maxSubArray(nums, start, mid)
        right_max_sum = self.maxSubArray(nums, mid+1, end)
        center_max_sum = self.maxCenterSum(nums, start, mid, end)
        
        return max(left_max_sum, right_max_sum, center_max_sum)
        
    def maxCenterSum(self, nums, start, mid, end):
        local_sum = 0
        left_sum = float("-inf")
        for i in range(mid, start-1, -1):
            local_sum += nums[i]
            left_sum = max(local_sum, left_sum)
        
        local_sum = 0
        right_sum = float("-inf")
        for i in range(mid+1, end+1):
            local_sum += nums[i]
            right_sum = max(local_sum, right_sum)
        
        center_sum = left_sum + right_sum
        return max(left_sum, right_sum,  center_sum)

        
