class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        right, left, answer = 0, 0, 0
        
        for right in range(len(s)):
            if s[right] in hashmap:
                left = max(left, hashmap[s[right]] + 1)
                
            hashmap[s[right]] = right 
            answer = max(answer, right - left + 1)
                
        return answer
