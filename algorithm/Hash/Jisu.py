class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 0
        res = 0
        tmp = set()
        while p2 < len(s):
            # 3 < 8
            # a b c a b c b b
            #               ^
            #             ^        
            # res = 3
            if s[p2] not in tmp:
                tmp.add(s[p2])
                p2 += 1
                res = max(res,p2-p1)
            else:
                tmp.remove(s[p1])
                p1+=1
        return res