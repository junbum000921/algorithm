n=int(input())
m=int(input())
s=input()
p="IOI"+"OI"*(n-1)
cnt=0
ans=0
for i in range(m):
    start=i
    if(s[start]=='I'):
        continue
    while (i < m-1 and s[i] != s[i+1]):
        i+=1
        
    end = i
    if s[i] == 'O':
        end-=1
    cnt=max(0,(end-start-len(p)+2)/2)
    ans+=cnt
print(ans)
