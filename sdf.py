##s=input()
##new_s=""
##for i in range(len(s)):
##    if s[i].isupper():
##        new_s+=s[i].lower()
##    else:
##        new_s+=s[i].upper()
##print(new_s)

from collections import Counter

n, m = map(int, input().split())  # 단어 개수, 최소 길이 제한
words = [input().strip() for _ in range(n)]

# 최소 길이 조건을 만족하는 단어만 필터링
filtered_words = [word for word in words if len(word) >= m]

# 단어 빈도수 계산
word_count = Counter(filtered_words)

# 정렬 기준 적용 (빈도수 내림차순, 길이 내림차순, 알파벳 오름차순)
sorted_words = sorted(word_count.keys(), key=lambda x: (-word_count[x], -len(x), x))

# 결과 출력
for word in sorted_words:
    print(word)
