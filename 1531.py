paper=[]
for i in range(101):
    paper.append([0]*101)
n,m=map(int,input().split())
arr=[]
cnt=0
for _ in range(n):
    x1,y1,x2,y2=map(int,input().split())
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            paper[y][x]+=1
for i in range(101):
    for j in range(101):
        if paper[i][j]>m:
            cnt+=1
print(cnt)

