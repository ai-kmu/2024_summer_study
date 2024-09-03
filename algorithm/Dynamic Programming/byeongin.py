class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -10000
        tmp = 0
        
        for i in nums :
            tmp += i

            if tmp >= i :
                if max_sum < tmp :
                    max_sum = tmp 

            else :
                tmp = i
                if max_sum < tmp :
                    max_sum = tmp

        return max_sum
