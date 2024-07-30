class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        price = 0
        cnt = 0

        for i in range(len(costs)):
            if (costs[i] + price <= coins):
                price += costs[i]
                cnt += 1
            else:
                break

        return cnt
