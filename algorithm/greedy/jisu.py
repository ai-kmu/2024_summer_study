class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ice_cnt = 0

        for c in costs:
            if c > coins:
                break
            coins -= c
            ice_cnt += 1

        return ice_cnt
