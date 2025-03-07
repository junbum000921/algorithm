# 입력 받기
N = int(input())
sums = []
for _ in range(N):
    sums.append(int(input()))

# 첫 번째 학생의 사탕 수를 기준으로 나머지 학생들의 사탕 수를 구함
total_sum = sum(sums)
first_student_candies = (total_sum - sum(sums[1::2])) // N

candies = [0] * N
candies[0] = first_student_candies

for i in range(1, N):
    candies[i] = sums[i - 1] - candies[i - 1]

# 각 학생의 사탕 수 출력
for candy in candies:
    print(candy)
