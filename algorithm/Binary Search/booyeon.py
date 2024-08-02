class Solution:

    def pivot(self, nums: List[int]) -> int: # pivot 구하기 (ft.binary)
        low = 0
        high = len(nums) - 1
        mid = low + (high - low) // 2
        
        while low != mid:
            if nums[mid] > nums[high]:
                low = mid
            else:
                high = mid
    
            mid = low + (high - low) // 2

        return len(nums)-(mid if nums[mid]<nums[high] else high)



    def search(self, nums: List[int], target: int) -> int:
        lowIDX = 0
        midIDX = len(nums)//2
        highIDX = len(nums) - 1

        term = self.pivot(nums)

        # ===
        
        for i in range(midIDX+1):
            midNum = nums[midIDX-term]
            if midNum == target:
                return (midIDX - term) % len(nums)
            elif midNum < target:
                lowIDX = midIDX
            else:
                highIDX = midIDX 

            midIDX = lowIDX + (highIDX - lowIDX)//2

        if nums[highIDX-term] == target:
                return (highIDX - term) % len(nums)

        return -1

