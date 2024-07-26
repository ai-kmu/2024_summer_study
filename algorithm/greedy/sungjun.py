class Solution:
    # icecream 이 n개 있다.
    # 최대한 많은 ice cream을 사고싶다.
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs = sorted(costs)
        ans = 0

        for cost in costs:
            if(coins < cost): break
            coins -= cost
            ans += 1

        return ans    
            
        
