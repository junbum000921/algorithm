import sys

# 체스판에서 알파벳(A-H)을 숫자로 변환하는 함수
def pos_to_coord(pos):
    return ord(pos[0]) - ord('A'), int(pos[1]) - 1

# 숫자 좌표를 체스 좌표(A1 형태)로 변환하는 함수
def coord_to_pos(x, y):
    return chr(x + ord('A')) + str(y + 1)

# 이동 방향 정의
directions = {
    "R": (1, 0), "L": (-1, 0), "B": (0, -1), "T": (0, 1),
    "RT": (1, 1), "LT": (-1, 1), "RB": (1, -1), "LB": (-1, -1)
}

# 입력 처리
king, stone, N = sys.stdin.readline().split()
N = int(N)

# 킹과 돌의 초기 위치 변환
kx, ky = pos_to_coord(king)
sx, sy = pos_to_coord(stone)

# N번의 이동 실행
for _ in range(N):
    move = sys.stdin.readline().strip()
    dx, dy = directions[move]

    # 킹이 이동할 위치 계산
    nkx, nky = kx + dx, ky + dy

    # 킹이 체스판 밖으로 나가는지 확인
    if not (0 <= nkx < 8 and 0 <= nky < 8):
        continue  # 이동 불가

    # 돌이 있는 곳으로 이동하면 돌도 같은 방향으로 이동
    if (nkx, nky) == (sx, sy):
        nsx, nsy = sx + dx, sy + dy
        # 돌이 체스판 밖으로 나가면 이동 불가
        if not (0 <= nsx < 8 and 0 <= nsy < 8):
            continue
        # 돌 이동
        sx, sy = nsx, nsy

    # 킹 이동
    kx, ky = nkx, nky

# 최종 위치 출력
print(coord_to_pos(kx, ky))
print(coord_to_pos(sx, sy))
