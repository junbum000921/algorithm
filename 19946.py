import math
n=int(input())
while True:
    if n%2==1:
        print(round(math.log2(n+1)))
        break
    n=n//2
    
