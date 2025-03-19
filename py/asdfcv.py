import sys

# 입력 받기
n, m, k = map(int, sys.stdin.readline().split())

# 빗물 누적을 위한 차이 배열 (Difference Array)
water = [0] * (n + 1)  # n+1을 사용하는 이유: t_i층까지 한 번에 누적하기 위함

for i in range(m):
    t, r = map(int, sys.stdin.readline().split())
    water[0] += r  # 1층부터 누적
    if t < n:
        water[t] -= r  # t+1층부터는 영향을 안 받도록 조정

# 빗물 누적 계산 & 무너지는 층 확인
current_water = 0  # 현재 층의 누적 빗물
for j in range(n):
    current_water += water[j]  # 누적합 계산
    if current_water > k:  # 한 번이라도 K 초과하면 즉시 출력 후 종료
        print(i, j + 1)
        exit()

# 모든 비가 와도 무너지는 층이 없을 경우
print(-1)
