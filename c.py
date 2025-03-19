import sys

# 입력 받기
N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
B = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]

# 3×3 변환 함수
def flip(x, y):
    for i in range(3):
        for j in range(3):
            A[x + i][y + j] ^= 1  # 0 <-> 1 뒤집기

# 연산 횟수 저장
count = 0

# 그리디 방식으로 3×3 변환 적용
for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:  # 값이 다르면 변환 수행
            flip(i, j)
            count += 1

# A가 B로 변환되었는지 확인
if A == B:
    print(count)
else:
    print(-1)
