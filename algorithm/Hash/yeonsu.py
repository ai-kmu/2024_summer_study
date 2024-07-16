class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_dict = {}
        max_len = 0
        start_index = 0

        for i, char in enumerate(s):
            if char in char_dict and char_dict[char] >= start_index:
                start_index = char_dict[char] + 1
                print(i, start_index)
            char_dict[char] = i
            max_len = max(max_len, i - start_index + 1)

        return max_len
