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

	  # 마지막에 두개만 남았을때 mid가 소수점을 버리기 때문에 왼쪽만 선택된다. 그래서 high도 확인해준다.
	  # mid와 high는 왼쪽부터의 위치이므로 전체에서 빼서 실제 인덱스를 구한다.
        return len(nums)-(mid if nums[mid]<nums[high] else high)


	# searching(binary search)
    def search(self, nums: List[int], target: int) -> int: 
        lowIDX = 0  # low index
        midIDX = len(nums)//2  # mid index
        highIDX = len(nums) - 1  # high index

        term = self.pivot(nums)  # random으로 결정된 pivot을 binary search로 구함.

        # === searching
        
        for i in range(midIDX+1):  # binary search의 최대 탐색횟수는 round(num/2) 일 것이다.
            # python은 음수인덱스를 지원하므로 pivot이 적용되지 않았다는 가정하에 진행
           # lowIDX, midIDX, highIDX는 pivot으로 이동하지 않았다는 가정하에 index를 저장한다.
            midNum = nums[midIDX-term] # 위치의 값을 확인하기 위한 변수
            if midNum == target:
                return (midIDX - term) % len(nums)  # index가 음수일 수 있기때문에 전체수로 나눈 나머지 사용
            elif midNum < target:
                lowIDX = midIDX
            else:  # midNum > target
                highIDX = midIDX 

            midIDX = lowIDX + (highIDX - lowIDX)//2

		# 위의 for문은 마지막에 두개만 남았을때 왼쪽만을 확인한다. 
		# 그러므로 오른쪽을 마저 확인해준다
        if nums[highIDX-term] == target:
                return (highIDX - term) % len(nums)
                
	  # 여기까지 왔다면 발견하지 못한 것
        return -1

