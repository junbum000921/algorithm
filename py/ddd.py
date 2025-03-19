t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    if n==1 or m==1:
        print("YES")
    elif n%2==1 or m%2==1:
        print("NO")
    else:
        print("YES")
