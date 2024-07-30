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
        
        
'''
다른 분들은 
line 7의 coins = coins - cost 를 coins -= cost 로 줄이거나,
if문을 for문 전체로 감싸는 형태,
while문을 사용하거나 
break대신 return문으로 한 형태가 있었다.

greedy를 직관적이게 잘 설명한 문제지만, 이번엔 다들 풀이가 비슷할 수 밖에 없는 점이 아쉽다.
'''
