class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a= dict()
        start = 0
        end = 0
        res = 0
        iter = 0
        for i in s :
            iter += 1
            # hash
            index = ord(i) - ord('a')
            if a.get(index) != None :
                if start < a.get(index) :
                    start = a.get(index)
            end += 1
            a[index] = iter
            res = max(res, end - start)
            

        return res
