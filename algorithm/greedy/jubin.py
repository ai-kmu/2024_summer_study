class Solution(object):
    def maxIceCream(self, costs, coins):
        idx = 0
        result = 0

        costs.sort()

        while coins > 0 and idx < len(costs) and costs[idx] <= coins:
            coins -= costs[idx]
            idx += 1
            result += 1
        
        return result
