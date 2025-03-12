a,b,c=map(int,input().split())
ab=a*b
ac=a*c
bc=b*c
abc=a*b*c
arr=[a,b,c,ab,ac,bc,abc]
arr.sort()
odd=[]
even=[]
for i in arr:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
if len(odd)==0:
    print(even[-1])
else:
    print(odd[-1])
