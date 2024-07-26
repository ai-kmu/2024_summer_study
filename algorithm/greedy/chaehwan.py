class Solution(object):
    def maxIceCream(self, costs, coins):
        cnt = 0
        costs.sort()
        for i in costs:
            if coins< i:
                return cnt
            cnt+=1
            coins-=i
        return cnt
        
