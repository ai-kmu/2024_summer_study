class Solution(object):

    """
    input:  List[int] nums
    output: List[List[int]] result
    
    : nums로 만들 수 있는 조합의 경우의 수를 반환
    ex) permute([1,2,3]) => [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    """
    def permute(self, nums):
        result = []  # 반환 값 저장
        if len(nums) < 3:  # 원소가 3개 미만인 경우
            if len(nums) == 2:  # 2개인 경우
                result = [nums, nums[::-1]]
            else:  # 1개 이하인 경우
                result = [nums]
        else:  # 원소가 3개 이상인 경우 
            # 앞자리 첫번째 원소만 바꾸고 남은 원소의 경우에 수를 더해 줌
            for idx, fn in enumerate(nums):  
                tmp = nums[idx+1:] + nums[:idx]  # 남은 원소로 이루어진 list
                tmpList = self.permute(tmp)
                for l in tmpList:
                    result.append([fn] + l)
            
        return result

