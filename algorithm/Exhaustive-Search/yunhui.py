class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        def backtrack(start, end):
            if start == end:
                answer.append(nums[:])
                
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]
                
        
        backtrack(0, len(nums))
        return answer
