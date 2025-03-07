import re

# 정규식 패턴
pattern = re.compile(r"^(100+1+|01)+$")

# 입력 받기
T = int(input())  # 테스트 케이스 개수
for _ in range(T):
    signal = input().strip()
    if pattern.fullmatch(signal):  # 정규식과 완벽히 일치하는지 검사
        print("YES")
    else:
        print("NO")
