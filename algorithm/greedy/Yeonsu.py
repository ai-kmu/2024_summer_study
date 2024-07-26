class Solution(object):
    def maxIceCream(self, costs, coins):
        costs = sorted(costs)
        cnt = 0

        for cost in costs:
            if coins >= cost:
                coins -= cost
                cnt += 1
            else:
                break
            
        return cnt
