n=int(input())
arr=[]
cnt=0
for _ in range(n):
    num,e=map(int,input().split())
    arr.append([num,e])
    if arr.count([num,1])==0 and e==0:
        cnt+=1
        print("Not entered but tried to out")
        arr.pop()
    if arr.count([num,1])==1 and e==0:
        arr.remove([num,1])
    if arr.count([num,1])==2 and e==1:      
        print("Already in but tried to enter")
        cnt+=1
        arr.pop()
    
print(cnt+len(arr))

    
