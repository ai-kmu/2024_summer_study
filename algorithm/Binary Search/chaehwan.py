class Solution(object):
    
    def search(self, nums, target):
        def findP(arr, start, end):
            if start + 1 == end:
                return end
            mid = (start + end) // 2
            if arr[start] > arr[mid]:
                return findP(arr, start, mid)
            elif arr[mid] > arr[end]:
                return findP(arr, mid, end)
            return 0 
        
        def bst(arr, start, end, target):
            if start > end:
                return -1
            mid = (start + end) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                return bst(arr, start, mid - 1, target)
            else:
                return bst(arr, mid + 1, end, target)
        
        pivot = findP(nums, 0, len(nums) - 1)
        
        if nums[pivot] <= target <= nums[len(nums) - 1]:
            return bst(nums, pivot, len(nums) - 1, target)
        else:
            return bst(nums, 0, pivot - 1, target)
