n=int(input())
x,y=map(int,input().split())
min_d=1000000000000000000
min_x=0
min_y=0
for _ in range(n-1):
    x1,y1=map(int,input().split())
    d=((x-x1)**2+(y-y1)**2)**(1/2)
    if d<min_d:
        min_d=d
        min_x=x1
        min_y=y1
print(x,y)
print(min_x,min_y)
print(round(min_d,2))
