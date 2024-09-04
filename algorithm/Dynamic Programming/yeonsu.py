class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 현재 부분 배열의 합과 최대 부분 배열의 합을 추적하는 변수
        current_sum = nums[0]
        max_sum = nums[0]
        
        # 배열의 첫 요소는 이미 사용했으므로 두 번째 요소부터 시작
        for i in range(1, len(nums)):
            # 현재 부분 배열의 합을 업데이트, 현재 값을 포함할지 여부 결정
            current_sum = max(nums[i], current_sum + nums[i])
            # 최대 부분 배열의 합을 업데이트
            max_sum = max(max_sum, current_sum)
        
        return max_sum
