class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        tmp = list()
        res = list()
        def recur(nums):
            for i in nums:
                tmp.append(i)
                num=nums[:]
                num.remove(i)
                if len(num) == 0:
                    res.append(tmp[:])
                recur(num)
                tmp.pop()
        recur(nums)

        return(res)