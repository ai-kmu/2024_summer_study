from typing import List

class Solution(object):
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start: int, end: int):
            if start == end:
                results.append(nums[:])
            for i in range(start, end):
                # 요소를 교환하여 새로운 순열을 만듭니다.
                nums[start], nums[i] = nums[i], nums[start]
                # 다음 요소로 재귀 호출을 통해 순열을 생성합니다.
                backtrack(start + 1, end)
                # 교환한 요소를 다시 원래대로 돌려놓습니다.
                nums[start], nums[i] = nums[i], nums[start]

        # 결과를 저장할 리스트
        results = []
        # 백트래킹 시작: 0부터 nums의 길이까지
        backtrack(0, len(nums))
        # 모든 가능한 순열이 저장된 results를 반환합니다.
        return results

# 예제 실행
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 3]
    print(solution.permute(nums1)) 
    nums2 = [0, 1]
    print(solution.permute(nums2)) 
    nums3 = [1]
    print(solution.permute(nums3)) 
