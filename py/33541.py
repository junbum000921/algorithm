n=int(input())

while True:
    n+=1
    if n==10000:
        print(-1)
        break
    n1=n//100
    n2=n%100
    if(n1+n2)**2==n:
        print(n)
        break
    
