class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        result = 0 # count
        
        for cost in costs:
            coins = coins - cost
            if coins < 0: # 탕진
                break
            result += 1

        return result
