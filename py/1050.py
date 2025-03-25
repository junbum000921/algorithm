import sys
from collections import defaultdict

INF = 1000000001

def solve():
    # 입력
    N, M = map(int, input().split())  # 시장에서 파는 재료의 수 N, 물약 제조법의 수 M
    price = {}  # 각 재료의 가격을 저장
    for _ in range(N):
        name, cost = input().split()
        price[name] = int(cost)
    
    # 물약 제조법
    potions = []
    for _ in range(M):
        formula = input().split()
        k = int(formula[0])  # 물약을 만드는 데 필요한 재료의 개수
        ingredients = []
        for i in range(1, len(formula), 2):
            num = int(formula[i])
            ing = formula[i+1]
            ingredients.append((num, ing))
        potions.append(ingredients)

    # 물약을 만드는 비용을 저장하는 딕셔너리
    cost = defaultdict(lambda: INF)
    
    # 시장에서 파는 재료의 가격은 그대로 사용
    for name in price:
        cost[name] = price[name]

    # DP 방식으로 물약 만들기
    def make_potion(name):
        if cost[name] != INF:
            return cost[name]  # 이미 계산된 비용이 있으면 리턴
        
        # 해당 물약을 만들 수 있는 방법을 찾아서 최소 비용 계산
        min_cost = INF
        for potion in potions:
            for qty, ingredient in potion:
                if ingredient == name:
                    potion_cost = 0
                    for qty, ingredient in potion:
                        potion_cost += qty * make_potion(ingredient)
                    min_cost = min(min_cost, potion_cost)
        
        cost[name] = min_cost
        return cost[name]

    result = make_potion("LOVE")
    
    if result >= INF:
        print(-1)
    elif result > 1000000000:
        print(1000000001)
    else:
        print(result)

solve()
