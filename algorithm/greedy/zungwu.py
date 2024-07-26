class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()     # 아이스크림 가격 리스트 costs를 오름차순으로 정렬
        icecream_count = 0      # 아이스크림의 개수를 저장할 변수를 0으로 초기화

        for cost in costs:
            if coins >= cost:       # 현재 코인 수가 아이스크림 가격 이상이면 구매
                coins -= cost       # 코인 수를 차감
                icecream_count += 1 # 아이스크림 개수 1씩 증가
            else:
                break       # 코인 수가 부족하면 반복문 종료
        
        return icecream_count

        costs = [1,3,2,4,1]
        coins = 7
        max_icecream = maxIceCream(costs, coins)
        print(f"아이스크림은 {max_icecream}개 만큼 구매할 수 있다.")

        costs = [10,6,8,7,7,8]
        coins = 5
        max_icecream = maxIceCream(costs, coins)
        print(f"아이스크림은 {max_icecream}개 만큼 구매할 수 있다.")

        costs = [1,6,3,1,2,5]
        coins = 20
        max_icecream = maxIceCream(costs, coins)
        print(f"아이스크림은 {max_icecream}개 만큼 구매할 수 있다.")
