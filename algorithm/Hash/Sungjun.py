class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        a = [-1] * 100  # 초기값을 -1로 설정
        start = 0

        for end in range(len(s)):
            # char to unicode int
            index = ord(s[end]) - ord('a')
            
            if a[index] >= start:  # 현재 문자가 이전에 등장한 경우
                start = a[index] + 1

            a[index] = end  # 현재 문자의 위치를 업데이트
            ans = max(ans, end - start + 1)  # 최대 길이를 업데이트

        return ans
