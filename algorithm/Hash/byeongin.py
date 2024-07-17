class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a= dict()
        start = 0
        end = 0
        res = 0
        iter = 0
        for i in s :
            iter += 1
            if a.get(i) != None :
                if start < a.get(i) :
                    start = a.get(i)
            end += 1
            a[i] = iter
            res = max(res, end - start)
        return res

