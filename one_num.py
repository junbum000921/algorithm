s=input()
if  len(s)<3:
    print(s)
elif len(s)==3:
    s=int(s)
    cnt=99
    for i in range(100,s+1):
        s0=i//100
        s1=i%100//10
        s2=i%100%10
        if (s0+s2)/2==s1:
            cnt+=1
    print(cnt)
else:
    print("144")
    
