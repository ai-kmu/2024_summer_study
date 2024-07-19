class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursive(a,b):
            if not b:
                res.append(a)
            else:
                for i in range(len(b)):
                    recursive(a + [b[i]], b[:i] + b[i+1:])
        res = []
        recursive([], nums)
        return res 
