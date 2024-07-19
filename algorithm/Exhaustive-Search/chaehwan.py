class Solution(object):
    def permute(self, nums):
        res = []
        def dfs(rem, cur):
            if not rem:
                res.append(list(cur))
                return
            for i in range(len(rem)):
                val = rem.pop(i)
                cur.append(val)
                dfs(rem, cur)
                cur.pop()
                rem.insert(i, val)
            return

        dfs(nums, [])
        return res
        


