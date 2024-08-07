class Solution(object):
    def search(self, nums, target):
        import math

        pivot = len(nums) - 1

        def find_pivot(nums, left, right):
            
            if left == right:
                return left
            
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                return find_pivot(nums, mid + 1, right)
            else:
                return find_pivot(nums, left, mid)

        def binary_search(nums, target, left, right):
            if left > right:
                return -1
            
            mid = (left+right) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                return binary_search(nums, target, mid + 1, right)
            else:
                return binary_search(nums, target, left, mid - 1)

        pivot = find_pivot(nums, 0, len(nums) - 1)
        answer = binary_search(nums, target, 0, pivot)

        if answer == -1:
            answer = binary_search(nums, target, pivot, len(nums) - 1)

        return answer
