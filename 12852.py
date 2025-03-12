def min_operations_to_one(N):
    dp = [0] * (N + 1)
    prev = [0] * (N + 1)

    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + 1
        prev[i] = i - 1
        
        if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
            prev[i] = i // 2
            
        if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
            prev[i] = i // 3

    # 최소 연산 횟수
    min_operations = dp[N]
    
    # 경로 추적
    path = []
    while N > 0:
        path.append(N)
        N = prev[N]



    return min_operations, path

# 입력 받기
N = int(input().strip())
min_ops, sequence = min_operations_to_one(N)

# 결과 출력
print(min_ops)
print(" ".join(map(str, sequence)))
