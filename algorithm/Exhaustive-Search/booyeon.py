class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        if len(nums) <= 3:
            for idx, fn in enumerate(nums):
                tmp = nums[idx+1:] + nums[:idx]
                if len(nums) == 2:
                    result = [nums, nums[::-1]]
                elif len(nums) <= 1:
                    result = [nums]
                else:
                    result += [[fn] + tmp, [fn] + tmp[::-1]]
        else:
            for idx, fn in enumerate(nums):
                tmp = nums[idx+1:] + nums[:idx]
                tmpList = self.permute(tmp)
                for l in tmpList:
                    result.append([fn] + l)
            
        return result

