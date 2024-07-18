class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = {}
        max_len = 0
        start = 0
        curr_len = 0

        for i, char in enumerate(s):
            if char in a:
                start = max(start, a[char] + 1)
            
            a[char] = i
            curr_len += 1

            max_len = max(max_len, curr_len-start)
            
        return max_len 