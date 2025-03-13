x,y=map(int,input().split())
diff=y-x
cnt=0
k=1
while diff>0:
    diff-=k
    cnt+=1
    if(cnt%2==0):
        k+=1

print(cnt)
