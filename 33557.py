T=int(input())
for _ in range(T):
    a,b=input().split()
    result=int(a)*int(b)
    s=""
    diff=len(a)-len(b)
    if diff>0:
        b="1"*diff+b
    elif diff<0:
        a="1"*(-diff)+a
    for i in range(len(a)):
        s+=str(int(a[i])*int(b[i]))
    if result==int(s):
        print(1)
    else:
        print(0)

