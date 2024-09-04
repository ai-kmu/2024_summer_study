# time limit~~

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(n!)
        # subarray = []
        crrMax = nums[0]
        for s in range(len(nums)):
            for e in range(s+1,len(nums)+1):
                subarraySum = sum(nums[s:e])
                if crrMax < subarraySum:
                    crrMax = subarraySum
                    # subarray = nums[s:e]

        return crrMax
