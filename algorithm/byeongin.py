class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
    
        while start <= end:
            mid = (start + end )// 2
            if nums[mid] == target :

                return mid
            elif nums[mid] > target : # left
                if (nums[start]<=nums[mid])&(nums[start] > target) : # left가 아닌 pivot된 right에 존재
                    start = mid + 1
                else:
                    end = mid - 1
            elif nums[mid] < target : # right
                if (nums[mid]<=nums[end])&(nums[end] < target) : # right가 아닌 pivot된 left에 존재
                    end = mid - 1
                else:
                    start = mid + 1

        return -1
