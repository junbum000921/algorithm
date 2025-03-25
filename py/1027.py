

#만약 제일 크기가 큰 높이를 가진 건물이 여러개면 제대로 출력 안됨.
#그래서 이렇게 하면 안된다.
#그리고 이렇게 하면 시간초과가 난다.
#그래서 이 문제는 스택을 이용해서 풀어야한다.
#스택을 이용해서 풀어보자.
#문제
#https://www.acmicpc.net/problem/1027
#입력
#첫째 줄에 빌딩의 개수 N이 주어진다. (1 ≤ N ≤ 50)
#
#둘째 줄에는 각 빌딩의 높이가 주어진다. 높이는 1,000,000,000보다 작거나 같은 자연수이다.
#
#출력
#첫째 줄에 보이는 빌딩의 개수를 출력한다.
n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    cnt=0
    for j in range(i+1,n):
        if i==j:
            continue
        ok=True
        for k in range(i+1,j):
            if (j-i)*a[k]-(j-k)*a[i]-(k-i)*a[j]>0:
                ok=False
                break
        if ok:
            cnt+=1
    ans=max(ans,cnt)
print(ans)

