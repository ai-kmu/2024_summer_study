class Solution(object):
    def search(self, nums, target):

        for idx in range(len(nums)):
            if nums[idx] == target:
                return idx
    
        return -1
