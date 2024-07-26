class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res = 0
        costs.sort()
        for i in costs :
            coins -= i 
            if coins < 0 :
                
                return res # 돈이 부족한 경우
            res += 1

        return res # 다 샀는데 돈이 남은 경우
