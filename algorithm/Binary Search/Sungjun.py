"""
target > mid or target < start and target < mid or target > end--> 무조건 반대쪽 
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        ans = -1

        while(start <= end):
            mid = (start + end) // 2

            # 종료조건
            if(nums[mid] == target):
                ans = mid
                break
            elif(nums[start] <= nums[mid]):
                if(target > nums[mid] or target < nums[start]):
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if(target < nums[mid] or target > nums[end]):
                    end = mid - 1
                else:
                    start = mid + 1

        return ans

