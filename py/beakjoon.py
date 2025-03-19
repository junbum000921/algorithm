a,b=map(int,input().split())
c=[]
cnt=0
for i in range(a):
    c.append(input())
for j in range(b):
    m=[]
    for j in range(a):
           m.append(c[j][i])
    print(m)
    if "X" not in c[i] and "X" not in m:
            cnt+=1
print(cnt)

    
