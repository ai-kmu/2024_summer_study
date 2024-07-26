class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()     

        for cost in costs:
            if coins >= cost:       
                coins -= cost       
                icecream_count += 1 
            else:
                break      
        
        return icecream_count
